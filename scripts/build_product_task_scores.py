#!/usr/bin/env python3
"""Build product × task economic scores from the repository datasets.

The script deliberately keeps:
- direct product evidence,
- cross-product family priors,
- exact historical model+harness evidence,
- active-human-time evidence,
- pricing evidence

as separate inputs. Capability-only observations never create P(success).

Run from the repository root:
    python3 scripts/build_product_task_scores.py
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

QUALITY = {"A": 1.0, "B": 0.8, "C": 0.6, "D": 0.4, "E": 0.2}
GRADE_RANK = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1}
GRADE_MARGIN = {"A": 0.05, "B": 0.08, "C": 0.12, "D": 0.18, "E": 0.25}
RELATIONSHIP_PRIOR_STRENGTH = 0.75
FAMILY_WEIGHT_CAP = 1.25
PRODUCT_PRIOR_STRENGTH = 1.50

RELATIONSHIP_SUCCESS_PRIOR = {
    "native": 0.68,
    "direct": 0.58,
    "connected": 0.52,
    "custom_workflow": 0.48,
    "backend": 0.40,
}
RELATIONSHIP_HUMAN_FACTOR = {
    "native": 0.85,
    "direct": 1.00,
    "connected": 1.05,
    "custom_workflow": 1.20,
    "backend": 1.35,
}

HARNESS_MAP = {
    "aider": ["Aider"],
    "claude-code": ["Claude Code"],
    "codex-cli": ["Codex CLI"],
    "cline": ["Cline CLI", "Cline"],
    "opencode": ["OpenCode"],
    "openhands": ["OpenHands"],
    "penguin-harness": ["PenguinHarness"],
    "deepseek-harness": ["DeepSeek Harness"],
    "qwen-code": ["Qwen Code"],
    "kimi-code": ["Kimi Code"],
    "gemini-cli": ["Gemini CLI"],
    "factory-droid": ["Factory Droid", "Droid"],
    "pi": ["Pi"],
    "mistral-vibe-code": ["Mistral Vibe Code"],
    "goose": ["Goose"],
    "jetbrains-junie": ["Junie"],
}

PER_USER_UNITS = {
    "user", "seat", "member", "license", "granted-seat", "developer",
    "contributing-developer", "active-contributor", "active-AI-user",
    "engineering-seat",
}
ORG_UNITS = {"organization", "workspace", "team", "site"}
PROJECT_UNITS = {"project"}


def load(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write("\n")


def sample_factor(n: int | float | None) -> float:
    if not n:
        return 0.65
    return max(0.5, min(1.5, math.log10(n + 1) / 3.0))


def plan_priority(name: str) -> int:
    n = (name or "").lower()
    if "enterprise" in n and "order" not in n:
        return 100
    if "business" in n:
        return 90
    if "teams" in n or "team" in n:
        return 80
    if "standard" in n:
        return 70
    if "pro" in n:
        return 60
    if "premium" in n:
        return 55
    if "core" in n:
        return 50
    if "max" in n:
        return 45
    if "starter" in n:
        return 40
    if "free" in n or "open-source" in n:
        return 5
    return 30


class Scorer:
    def __init__(self, root: Path, args: argparse.Namespace) -> None:
        self.root = root
        self.args = args
        self.tasks = load(root / "data/tasks.json")
        self.task_by = {x["id"]: x for x in self.tasks}
        self.pricing = load(root / "data/pricing/catalog.json")["records"]
        self.price_by = {x["solution_id"]: x for x in self.pricing}
        self.product_obs = load(root / "data/evidence/public-product-observations.json")
        self.family_obs = load(root / "data/evidence/public-family-observations.json")
        self.old_obs = load(root / "data/observations.json")
        self.family_relevance = load(root / "data/evidence/task-product-family-relevance.json")["families"]
        self.mapping = load(root / "data/task-solution-map/all-current.json")

        self.fx = {
            "EUR": 1.0,
            "USD": 1.0 / args.eur_usd,
            "CNY": 1.0 / args.eur_cny,
        }

    def eur(self, value: float | None, currency: str) -> float | None:
        if value is None:
            return None
        return value * self.fx.get(currency, self.fx["USD"])

    def monthly_public_plan(self, rec: dict[str, Any]) -> dict[str, Any] | None:
        plans = [
            p for p in rec.get("plans", [])
            if p.get("amount") is not None
            and p.get("period") in {"month", "year"}
            and p.get("unit") not in {"usage", "once"}
        ]
        plans.sort(key=lambda p: (-plan_priority(p.get("name", "")), p["amount"]))
        if not plans:
            return None

        p = plans[0]
        monthly = self.eur(p["amount"], p.get("currency", "USD"))
        if p["period"] == "year":
            monthly /= 12

        unit = p.get("unit")
        if unit in PER_USER_UNITS:
            div = 1
        elif unit in ORG_UNITS:
            div = self.args.users
        elif unit in PROJECT_UNITS:
            div = self.args.project_users
        else:
            return None

        value = monthly / div
        return {"point": value, "low": value, "high": value, "basis": p["name"]}

    def monthly_estimate(self, rec: dict[str, Any]) -> dict[str, Any] | None:
        e = rec.get("estimated_enterprise_cost")
        if not e:
            return None
        if e.get("period") in {"usage", "once"}:
            return None

        low = self.eur(e["low"], e.get("currency", "USD"))
        point = self.eur(e["typical"], e.get("currency", "USD"))
        high = self.eur(e["high"], e.get("currency", "USD"))

        if e.get("period") == "year":
            low, point, high = low / 12, point / 12, high / 12

        unit = e.get("unit")
        if unit == "organization":
            div = self.args.users
        elif unit == "project":
            div = self.args.project_users
        else:
            div = 1

        return {
            "point": point / div,
            "low": low / div,
            "high": high / div,
            "basis": "sensitivity estimate normalized",
        }

    def fixed_cost(self, rec: dict[str, Any]) -> dict[str, Any]:
        return (
            self.monthly_public_plan(rec)
            or self.monthly_estimate(rec)
            or {"point": 0.0, "low": 0.0, "high": 0.0, "basis": "no fixed component"}
        )

    def published_token_cost(self, rec: dict[str, Any], task: dict[str, Any]) -> dict[str, Any] | None:
        plans = rec.get("plans", [])
        inp = next(
            (p for p in plans
             if "input" in p.get("name", "").lower()
             and p.get("unit") == "1M tokens"
             and p.get("amount") is not None),
            None,
        )
        out = next(
            (p for p in plans
             if "output" in p.get("name", "").lower()
             and p.get("unit") == "1M tokens"
             and p.get("amount") is not None),
            None,
        )
        work = task.get("workload", {})
        if not inp or work.get("inputTokens") is None:
            return None

        value = self.eur(inp["amount"], inp.get("currency", "USD")) * work["inputTokens"] / 1e6
        if out:
            value += self.eur(out["amount"], out.get("currency", "USD")) * work.get("outputTokens", 0) / 1e6
        return {"point": value, "low": value * 0.8, "high": value * 1.3, "basis": "published token rates"}

    def generic_external_cost(self, task: dict[str, Any]) -> dict[str, Any]:
        work = task.get("workload", {})
        usd = (
            work.get("inputTokens", 0) / 1e6 * self.args.byok_input_usd_m
            + work.get("outputTokens", 0) / 1e6 * self.args.byok_output_usd_m
        )
        point = self.eur(usd, "USD")
        return {
            "point": point,
            "low": point * self.args.byok_low_factor,
            "high": point * self.args.byok_high_factor,
            "basis": "generic external-model proxy",
        }

    def empirical_harness_cost(self, solution_id: str, task: dict[str, Any]) -> dict[str, Any] | None:
        harnesses = HARNESS_MAP.get(solution_id)
        if not harnesses:
            return None
        values = sorted(
            o["api"] for o in self.old_obs
            if o.get("harness") in harnesses
            and o.get("api") is not None
            and task.get("weights", {}).get(o.get("family"), 0) >= 0.2
        )
        if not values:
            return None
        usd = values[len(values) // 2]
        point = self.eur(usd, "USD")
        return {
            "point": point,
            "low": point * 0.6,
            "high": point * 1.6,
            "basis": f"median API cost ({len(values)} relevant observations)",
        }

    def service_cost(self, rec: dict[str, Any], task: dict[str, Any], solution_id: str) -> dict[str, Any]:
        fixed = self.fixed_cost(rec)
        task_hours = task["humanNo"] / 60.0

        point_fixed = fixed["point"] / self.args.ai_hours_month * task_hours
        low_fixed = fixed["low"] / self.args.ai_hours_month_low_cost * task_hours
        high_fixed = fixed["high"] / self.args.ai_hours_month_high_cost * task_hours

        variable = self.published_token_cost(rec, task)
        if variable is None and rec.get("inference_cost") in {"byok_external", "self_host_compute"}:
            variable = self.empirical_harness_cost(solution_id, task) or self.generic_external_cost(task)
        elif variable is None and rec.get("inference_cost") == "mixed" and fixed["point"] == 0:
            variable = self.empirical_harness_cost(solution_id, task) or self.generic_external_cost(task)

        if variable is None:
            variable = {"point": 0.0, "low": 0.0, "high": 0.0, "basis": "bundled/no variable modeled"}

        partial = (
            any(v.get("amount") is None for v in rec.get("variable_charges", []))
            or rec.get("inference_cost") == "unknown"
        )

        return {
            "point": point_fixed + variable["point"],
            "low": low_fixed + variable["low"],
            "high": (high_fixed + variable["high"]) * (1.35 if partial else 1.0),
            "fixed_point": point_fixed,
            "variable_point": variable["point"],
            "fixed_basis": fixed["basis"],
            "variable_basis": variable["basis"],
            "partial": partial,
        }

    def family_prior(self, task: dict[str, Any], relationship: str) -> dict[str, Any]:
        base = RELATIONSHIP_SUCCESS_PRIOR.get(relationship, 0.45)
        groups: dict[str, list[tuple[dict[str, Any], float]]] = defaultdict(list)

        for o in self.family_obs:
            if o.get("probability_proxy") is None:
                continue
            relevance = self.family_relevance.get(o["family"], {}).get(task["id"], 0)
            if relevance < 0.2:
                continue
            weight = QUALITY.get(o.get("source_grade", "E"), 0.2) * relevance * sample_factor(o.get("n"))
            groups[o["family"]].append((o, weight))

        sw = sp = 0.0
        evidence_ids: list[str] = []
        for observations in groups.values():
            total = sum(w for _, w in observations)
            scale = min(1.0, FAMILY_WEIGHT_CAP / total) if total else 1.0
            for o, raw_weight in observations:
                weight = raw_weight * scale
                sw += weight
                sp += weight * o["probability_proxy"]
                evidence_ids.append(o["id"])

        point = (RELATIONSHIP_PRIOR_STRENGTH * base + sp) / (RELATIONSHIP_PRIOR_STRENGTH + sw)
        return {"point": point, "base": base, "weight": sw, "observations": evidence_ids}

    def direct_success_rows(self, solution_id: str, task: dict[str, Any]) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []

        for o in self.product_obs:
            if o.get("solution_id") != solution_id or o.get("probability_proxy") is None:
                continue
            relevance = self.family_relevance.get(o["family"], {}).get(task["id"], 0)
            if relevance >= 0.2:
                rows.append({
                    "id": o["id"], "p": o["probability_proxy"], "grade": o.get("source_grade", "C"),
                    "rel": relevance, "n": o.get("n"),
                    "cluster": o.get("independence_cluster", o["id"]),
                })

        harnesses = HARNESS_MAP.get(solution_id, [])
        for i, o in enumerate(self.old_obs):
            if o.get("harness") not in harnesses or not o.get("probLike"):
                continue
            relevance = task.get("weights", {}).get(o.get("family"), 0)
            if relevance >= 0.2:
                rows.append({
                    "id": f"historical:{i}",
                    "p": max(0.0, min(1.0, o.get("score", 0) / 100.0)),
                    "grade": o.get("sourceGrade", o.get("grade", "D")),
                    "rel": relevance,
                    "n": o.get("n"),
                    "cluster": f"{o.get('benchmark')}|{o.get('version')}",
                })
        return rows

    def success(self, solution_id: str, task: dict[str, Any], relationship: str) -> dict[str, Any]:
        fp = self.family_prior(task, relationship)
        clusters: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for e in self.direct_success_rows(solution_id, task):
            e = dict(e)
            e["w"] = QUALITY.get(e["grade"], 0.2) * e["rel"] * sample_factor(e.get("n"))
            clusters[e["cluster"]].append(e)

        sw = sp = sq = 0.0
        used: list[dict[str, Any]] = []
        for rows in clusters.values():
            total = sum(x["w"] for x in rows)
            scale = min(1.0, 1.2 / total) if total else 1.0
            for x in rows:
                weight = x["w"] * scale
                sw += weight
                sp += weight * x["p"]
                sq += weight * QUALITY.get(x["grade"], 0.2)
                used.append({**x, "effective_weight": weight})

        p = (PRODUCT_PRIOR_STRENGTH * fp["point"] + sp) / (PRODUCT_PRIOR_STRENGTH + sw)

        relative_adjustment = 0.0
        for o in self.product_obs:
            if o.get("solution_id") != solution_id or o.get("relative_success_delta") is None:
                continue
            relevance = self.family_relevance.get(o["family"], {}).get(task["id"], 0)
            if relevance < 0.2:
                continue
            relative_adjustment += math.copysign(
                min(0.10, abs(o["relative_success_delta"]) * relevance * QUALITY.get(o.get("source_grade", "E"), 0.2) * 0.5),
                o["relative_success_delta"],
            )

        relative_adjustment = max(-0.10, min(0.10, relative_adjustment))
        p = max(0.05, min(0.95, p * (1 + relative_adjustment)))

        average_quality = sq / sw if sw else 0
        grade = "E"
        if sw >= 1.4 and average_quality >= 0.72 and len(clusters) >= 2:
            grade = "B"
        elif sw >= 0.65:
            grade = "C"
        elif sw > 0 or fp["weight"] >= 0.55:
            grade = "D"

        margin = GRADE_MARGIN[grade]
        return {
            "point": p,
            "low": max(0.05, p - margin),
            "high": min(0.95, p + margin),
            "relationship_prior": fp["base"],
            "family_prior": fp["point"],
            "family_prior_weight": fp["weight"],
            "family_prior_observations": fp["observations"],
            "grade": grade,
            "clusters": len(clusters),
            "weight": sw,
            "observations": [x["id"] for x in used],
            "prior_driven": sw < 0.65,
            "secondary_adjustment": relative_adjustment,
        }

    def relevant_product_evidence(self, solution_id: str, task: dict[str, Any]) -> list[dict[str, Any]]:
        return [
            {
                "id": o["id"],
                "grade": o.get("source_grade", "E"),
                "family": o["family"],
                "type": o.get("evidence_type"),
                "metric": o.get("metric"),
            }
            for o in self.product_obs
            if o.get("solution_id") == solution_id
            and self.family_relevance.get(o["family"], {}).get(task["id"], 0) >= 0.2
        ]

    def human_time(self, solution_id: str, task: dict[str, Any], relationship: str) -> dict[str, Any]:
        relation_factor = RELATIONSHIP_HUMAN_FACTOR.get(relationship, 1.2)
        factor = 1.0
        direct: list[dict[str, Any]] = []
        family: list[dict[str, Any]] = []

        for o in self.family_obs:
            if o.get("human_time_multiplier") is None:
                continue
            relevance = self.family_relevance.get(o["family"], {}).get(task["id"], 0)
            if relevance < 0.2:
                continue
            reduction = (
                (1 - o["human_time_multiplier"]) * relevance
                * QUALITY.get(o.get("source_grade", "E"), 0.2) * 0.35
            )
            factor *= max(0.6, 1 - reduction)
            family.append({"id": o["id"], "grade": o.get("source_grade", "E"), "rel": relevance})

        for o in self.product_obs:
            if o.get("solution_id") != solution_id or o.get("human_time_multiplier") is None:
                continue
            relevance = self.family_relevance.get(o["family"], {}).get(task["id"], 0)
            if relevance < 0.2:
                continue
            reduction = (
                (1 - o["human_time_multiplier"]) * relevance
                * QUALITY.get(o.get("source_grade", "E"), 0.2) * 0.75
            )
            factor *= max(0.45, 1 - reduction)
            direct.append({"id": o["id"], "grade": o.get("source_grade", "E"), "rel": relevance})

        grade = "D"
        all_ev = direct + family
        if all_ev:
            best = max(all_ev, key=lambda x: GRADE_RANK[x["grade"]])
            grade = best["grade"]
            if not direct:
                grade = {"A": "B", "B": "C", "C": "D", "D": "D", "E": "D"}[grade]
            if best["rel"] < 0.5 and GRADE_RANK[grade] > 1:
                grade = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "E"}[grade]

        return {
            "point": task["humanAI"] * relation_factor * factor,
            "low": task["humanAIlo"] * relation_factor * max(0.5, factor * 0.85),
            "high": task["humanAIhi"] * relation_factor * min(1.5, factor * 1.15),
            "baseline": task["humanAI"],
            "relationship_factor": relation_factor,
            "evidence_factor": factor,
            "observations": [x["id"] for x in direct],
            "family_observations": [x["id"] for x in family],
            "grade": grade,
        }

    def human_only(self, task: dict[str, Any]) -> dict[str, float]:
        return {
            "point": task["humanNo"] / 60 * self.args.human_rate,
            "low": task["humanNolo"] / 60 * self.args.human_rate,
            "high": task["humanNohi"] / 60 * self.args.human_rate,
        }

    @staticmethod
    def economic(human_only_cost: float, active_human_min: float, service_cost: float, p: float, human_rate: float) -> dict[str, float]:
        attempt = service_cost + active_human_min / 60 * human_rate
        success = attempt / max(0.05, p)
        return {
            "attempt": attempt,
            "success": success,
            "meta": 100 * human_only_cost / (human_only_cost + success),
            "profit": human_only_cost / success,
        }

    @staticmethod
    def weakest_grade(grades: list[str]) -> str:
        return min(grades, key=lambda x: GRADE_RANK[x])

    def build(self) -> tuple[list[dict[str, Any]], dict[str, Any]]:
        scores: list[dict[str, Any]] = []

        for task_map in self.mapping:
            task = self.task_by.get(task_map["task_id"])
            if not task:
                continue
            human_only = self.human_only(task)

            for candidate in task_map["candidates"]:
                rec = self.price_by.get(candidate["solution_id"])
                if not rec:
                    continue

                solution_id = candidate["solution_id"]
                relationship = candidate["relationship"]
                success = self.success(solution_id, task, relationship)
                human_time = self.human_time(solution_id, task, relationship)
                service = self.service_cost(rec, task, solution_id)

                point = self.economic(human_only["point"], human_time["point"], service["point"], success["point"], self.args.human_rate)
                pessimistic = self.economic(human_only["low"], human_time["high"], service["high"], success["low"], self.args.human_rate)
                optimistic = self.economic(human_only["high"], human_time["low"], service["low"], success["high"], self.args.human_rate)

                cost_grade = rec.get("confidence", {}).get("grade", "E")
                direct_evidence = self.relevant_product_evidence(solution_id, task)

                scores.append({
                    "task_id": task["id"],
                    "task_label": task["label"],
                    "domain": task["domain"],
                    "solution_id": solution_id,
                    "solution_name": rec["solution_name"],
                    "vendor": rec["vendor"],
                    "category": rec["category"],
                    "relationship": relationship,
                    "success_probability": success,
                    "human_active_minutes": human_time,
                    "service_cost_eur_attempt": service,
                    "human_only_cost_eur": human_only,
                    "expected_cost_success_eur": {
                        "point": point["success"],
                        "low": optimistic["success"],
                        "high": pessimistic["success"],
                    },
                    "meta_score": {
                        "point": point["meta"],
                        "low": pessimistic["meta"],
                        "high": optimistic["meta"],
                    },
                    "profitability_factor": {
                        "point": point["profit"],
                        "low": pessimistic["profit"],
                        "high": optimistic["profit"],
                    },
                    "pricing": {
                        "status": rec["pricing_status"],
                        "grade": cost_grade,
                        "model_confidence": rec.get("confidence", {}).get("pricing_model"),
                        "monetary_confidence": rec.get("confidence", {}).get("monetary"),
                        "bundle_id": rec.get("commercial_bundle_id"),
                    },
                    "evidence": {
                        "success_grade": success["grade"],
                        "human_time_grade": human_time["grade"],
                        "cost_grade": cost_grade,
                        "meta_confidence_grade": self.weakest_grade([success["grade"], human_time["grade"], cost_grade]),
                        "direct_product_observations": direct_evidence,
                        "success_observations": success["observations"],
                        "family_prior_observations": success["family_prior_observations"],
                        "independent_success_clusters": success["clusters"],
                        "success_coverage_weight": success["weight"],
                    },
                    "prior_driven": {
                        "success": success["prior_driven"],
                        "human_time": not human_time["observations"] and not human_time["family_observations"],
                        "cost": rec["pricing_status"] == "contact_sales",
                    },
                    "scoring_version": self.args.version,
                })

        scores.sort(key=lambda x: (x["domain"], x["task_id"], -x["meta_score"]["point"]))

        task_summary: dict[str, Any] = {}
        for task in self.tasks:
            rows = sorted(
                (x for x in scores if x["task_id"] == task["id"]),
                key=lambda x: -x["meta_score"]["point"],
            )
            empirical = [
                x for x in rows
                if x["evidence"]["direct_product_observations"]
                or not x["success_probability"]["prior_driven"]
            ]

            def simple(x: dict[str, Any]) -> dict[str, Any]:
                return {
                    "solution_id": x["solution_id"],
                    "solution_name": x["solution_name"],
                    "meta_score": round(x["meta_score"]["point"], 2),
                    "range": [round(x["meta_score"]["low"], 2), round(x["meta_score"]["high"], 2)],
                    "p_success": round(x["success_probability"]["point"], 3),
                    "relationship_prior": round(x["success_probability"]["relationship_prior"], 3),
                    "family_prior": round(x["success_probability"]["family_prior"], 3),
                    "success_grade": x["evidence"]["success_grade"],
                    "human_time_grade": x["evidence"]["human_time_grade"],
                    "meta_confidence_grade": x["evidence"]["meta_confidence_grade"],
                    "relationship": x["relationship"],
                }

            confidence_counts: dict[str, int] = defaultdict(int)
            for row in rows:
                confidence_counts[row["evidence"]["meta_confidence_grade"]] += 1

            task_summary[task["id"]] = {
                "task_label": task["label"],
                "domain": task["domain"],
                "candidate_count": len(rows),
                "success_empirical_count": sum(not x["success_probability"]["prior_driven"] for x in rows),
                "direct_product_evidence_count": sum(bool(x["evidence"]["direct_product_observations"]) for x in rows),
                "family_prior_supported_count": sum(bool(x["success_probability"]["family_prior_observations"]) for x in rows),
                "meta_confidence_counts": dict(confidence_counts),
                "top_by_point_estimate": [simple(x) for x in rows[:10]],
                "top_with_direct_or_success_evidence": [simple(x) for x in empirical[:10]],
            }

        index = {
            "schema_version": 5,
            "generated_at": "2026-09-27",
            "scoring_version": self.args.version,
            "task_count": len(self.tasks),
            "solution_count": len(self.pricing),
            "scored_pairs": len(scores),
            "human_rate_eur_h": self.args.human_rate,
            "reference_users": self.args.users,
            "reference_ai_eligible_hours_per_user_month": self.args.ai_hours_month,
            "fx": {"date": "2026-09-25", "EURUSD": self.args.eur_usd, "EURCNY": self.args.eur_cny},
            "prior_strength": PRODUCT_PRIOR_STRENGTH,
            "relationship_prior_strength": RELATIONSHIP_PRIOR_STRENGTH,
            "family_weight_cap": FAMILY_WEIGHT_CAP,
            "relationship_success_priors": RELATIONSHIP_SUCCESS_PRIOR,
            "relationship_human_time_factors": RELATIONSHIP_HUMAN_FACTOR,
            "family_benchmark_count": len(self.family_obs),
            "product_evidence_count": len(self.product_obs),
            "files": [f"data/task-scores/{d}.json" for d in sorted({t["domain"] for t in self.tasks})],
            "task_summary": task_summary,
            "warnings": [
                "Family benchmarks modify priors only; they are never attributed as direct product performance.",
                "Capability-only evidence never creates P(success).",
                "Product-level scores do not replace exact model+harness+configuration scores.",
                "P(success), active-human time and monetary cost have separate confidence grades.",
                "Meta confidence is conservatively the weakest of success, human-time and cost confidence.",
                "Prior-driven rows are hypotheses requiring benchmarking, not proven performance.",
                "Quote-only pricing uses sensitivity estimates, never vendor-list-price claims.",
                "Fixed subscription cost is amortized using the declared reference workload.",
                "Bundle/prerequisite rules must be applied when composing multi-product stacks.",
            ],
        }
        return scores, index


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument("--version", default="product-task-v1.7")
    p.add_argument("--human-rate", type=float, default=50.0)
    p.add_argument("--users", type=int, default=50)
    p.add_argument("--project-users", type=int, default=10)
    p.add_argument("--ai-hours-month", type=float, default=80.0)
    p.add_argument("--ai-hours-month-low-cost", type=float, default=120.0)
    p.add_argument("--ai-hours-month-high-cost", type=float, default=40.0)
    p.add_argument("--eur-usd", type=float, default=1.1403)
    p.add_argument("--eur-cny", type=float, default=7.6551)
    p.add_argument("--byok-input-usd-m", type=float, default=2.0)
    p.add_argument("--byok-output-usd-m", type=float, default=10.0)
    p.add_argument("--byok-low-factor", type=float, default=0.35)
    p.add_argument("--byok-high-factor", type=float, default=3.0)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    scorer = Scorer(args.root, args)
    scores, index = scorer.build()

    domains = sorted({t["domain"] for t in scorer.tasks})
    for domain in domains:
        dump(
            args.root / f"data/task-scores/{domain}.json",
            [x for x in scores if x["domain"] == domain],
        )
    dump(args.root / "data/task-scores/index.json", index)

    confidence: dict[str, int] = defaultdict(int)
    for row in scores:
        confidence[row["evidence"]["meta_confidence_grade"]] += 1

    print(json.dumps({
        "scored_pairs": len(scores),
        "direct_product_evidence_pairs": sum(bool(x["evidence"]["direct_product_observations"]) for x in scores),
        "family_prior_supported_pairs": sum(bool(x["success_probability"]["family_prior_observations"]) for x in scores),
        "success_empirical_pairs": sum(not x["success_probability"]["prior_driven"] for x in scores),
        "meta_confidence_counts": dict(confidence),
    }, indent=2))


if __name__ == "__main__":
    main()
