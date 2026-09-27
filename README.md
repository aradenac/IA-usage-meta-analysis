# IA Usage Meta-Analysis

Meta-analysis of AI solutions for real embedded-software engineering activities.

The project asks a practical question:

> **For task T, which AI solution/configuration should an engineer use, and is it economically preferable to doing the work without AI?**

## Current scope

The taxonomy is tailored to embedded-software teams working across:

- C/C++, MCU/MPU, Zephyr RTOS, embedded Linux, FreeRTOS, ThreadX, ESP-IDF, bare metal, AUTOSAR, Yocto/BitBake and Buildroot;
- V-cycle software engineering, requirements traceability, architecture, detailed design and verification;
- GitLab, GitLab CI, Docker, HIL benches, Jira, Confluence, SharePoint and Reqtify;
- automotive constraints such as Automotive SPICE, ISO 26262 and coding rules;
- industrial IoT and cybersecurity, including CRA, secure-by-design/default, PKI, TARA, SBOM and vulnerability management;
- technical research, technology watch and continuous learning.

## Repository layout

- `site/index.html` — current standalone interactive report.
- `data/` — structured data extracted from the report.
- `docs/` — methodology and data-model documentation.
- `evidence/` — place for reproducible benchmark evidence, field signals and future internal tests.

## Website deployment

The static report can be deployed automatically to Cloudflare Pages through
GitHub Actions. See [`docs/cloudflare-pages.md`](docs/cloudflare-pages.md) for
the one-time Cloudflare setup, required GitHub secrets, and deployment
behavior.

## Important status

The business taxonomy is now much richer than the original public benchmark taxonomy. Many current task estimates therefore still reuse the closest historical benchmark families as **provisional proxies**. The next phase of the project is to collect task-specific evidence and add broader user-facing AI solutions, not only coding harnesses.

Reliability/confidence remains separate from the economic MetaScore.
