Thanks for wanting to help — this file explains the fastest way to contribute useful work.

Quick note from the maintainer
- The project is run by a solo maintainer who has a traumatic brain injury (TBI). Please be patient and kind — small, clear PRs and short, explicit questions are the best way to help.

How to start
1. Fork the repo and create a branch for your work:
   - git checkout -b feat/yourname-short-desc
2. Target branch for PRs: feature/sdk-mvp
   - Open PRs should target feature/sdk-mvp so changes can be reviewed and grouped.

Development workflow
- Install dependencies (if present):
  - python -m venv .venv
  - source .venv/bin/activate  # or .venv\Scripts\activate on Windows
  - pip install -r requirements file exists
- Run tests:
  - python -m pytest
- Format code:
  - black .  (optional but appreciated)

What to work on (small, focused contributions)
- See the pinned “Help wanted” issue for prioritized tasks (parse, mount, adapters, tests, CI).
- Pick one small logical change per PR).
- Use clear commit messages, e.g., feat: add MockAdapter or fix(doctrine): handle empty laws.
- Include a short description and testing notes in the PR body.
- If your change needs review, request a reviewer in the PR.

Testing & CI
- Add pytest tests for any behavior you change or add.
- CI runs on push/PR — make sure tests pass locally before opening a PR.

Communication
- If you’re unsure about a task, open an issue or comment on a help-wanted issue before starting.
- Be explicit about what you need reviewed or if you need pairing help.
- The maintainer will respond but may need extra time; patience is appreciated.

Non-code contributions
- Docs, examples, test cases, and issue triage are extremely valuable.
- If you can’t code but want to help coordinate contributors, comment on the help-wanted issue.

Credit & maintenance
- Contributors will be credited in the README.
- Sustained contributors may be invited as co-maintainers.

License
- This project uses the repository’s chosen license. Check LICENSE in the repo root.

Security & privacy
- Never include API keys, secrets, or personal/private data in PRs or issues.
- If you discover a security issue, open a private issue and label it “security” if possible.

Thank you
- Small contributions move this project forward. If you want guidance, mention the task number in an issue or open a draft PR and I’ll help refine it.
