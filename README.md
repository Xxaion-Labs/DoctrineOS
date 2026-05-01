# DoctrineOS

[![Validate DoctrineOS](https://github.com/Xxaion-Labs/DoctrineOS/actions/workflows/validate.yml/badge.svg)](https://github.com/Xxaion-Labs/DoctrineOS/actions/workflows/validate.yml)

```text
⧉
```

**DoctrineOS is an AGPL operating system prototype for the post-app age of AI: sovereign computing where intelligence is native, behavior is governed by mountable tesseracts, and the user remains the root of power.**

Version: 0.1.0 Prototype  
License: AGPLv3-or-later

## What `⧉` means

`⧉` is the public symbol for a tesseract.

The symbol is the object. In prose, call it **a tesseract**.

A tesseract is a semantic-machine object that can carry human-readable meaning, machine-readable structure, mountable runtime context, and inspectable proof surfaces.

The current public compatibility surface is `.doctrine`.

See [⧉](TESSERACT.md).

## What this is

DoctrineOS is a public AI-native operating system prototype built around tesseracts.

It is not a chatbot, wrapper, plugin, desktop assistant, or agent demo. It is the beginning of a user-governed computing environment where AI is part of the operating layer itself and `.doctrine` supplies the current public tesseract compatibility surface.

## What it unlocks

DoctrineOS moves AI from an app-shaped box into a governed operating surface:

- the user remains root authority
- tesseracts define operating behavior
- actions are capability-scoped
- permissioned actions emit receipts
- runtime state stays inspectable
- adapters connect models, files, tools, apps, and services
- public code remains open under AGPLv3-or-later

## Current status

DoctrineOS currently includes:

- SDK and CLI support for the public `.doctrine` compatibility surface
- `.doctrine` loading, parsing, validation, and mounting
- mount receipts with context hashes
- public concept nodes and generated node registry
- adapter examples
- DoctrineOS prototype shell
- default DoctrineOS profile
- action receipts and runtime state logging
- GitHub Actions validation

## DoctrineOS prototype shell

The `doctrineos` command is the first runnable DoctrineOS control surface.

It loads a profile, mounts it, plans command intent, identifies needed capabilities, asks for permission where required, routes approved commands to safe adapters, writes action receipts, and records runtime state.

```bash
doctrineos --json
doctrineos inspect workspace
doctrineos --yes inspect workspace
```

Runtime state and receipts are written under `.doctrineos/` by default.

## Quick start

```bash
git clone https://github.com/Xxaion-Labs/DoctrineOS.git
cd DoctrineOS
pip install -e .
```

Mount the standard public tesseract-compatible file:

```bash
doctrine mount standard_public_template.doctrine
```

Run the DoctrineOS prototype shell:

```bash
doctrineos --json
doctrineos inspect workspace
```

Validate the example node:

```bash
doctrine validate nodes/example.md
```

Build the public node registry:

```bash
doctrine registry build
```

Use the SDK directly:

```python
from doctrine import Doctrine

doctrine = Doctrine.load("standard_public_template")
receipt = doctrine.mount()
print(receipt["instruction_context"])
```

## Project map

- [⧉](TESSERACT.md) — public standard for the tesseract symbol and object class
- [Vision](VISION.md) — why DoctrineOS exists
- [Architecture](ARCHITECTURE.md) — system layers and control spine
- [Roadmap](ROADMAP.md) — build path from prototype to public OS environment
- [Prototype Shell](docs/prototype-shell.md) — runnable shell guide
- [Specification](SPEC.md) — `.doctrine` compatibility surface, mounting, validation, and receipts
- [Compatibility](COMPATIBILITY.md) — public compatibility requirements
- [Examples](examples/README.md) — adapter and workflow examples
- [Nodes](nodes/README.md) — public concept node library
- [Changelog](CHANGELOG.md) — release history
- [Contributing](CONTRIBUTING.md) — contribution guide

## Repository structure

- `TESSERACT.md` — public `⧉` standard
- `standard_public_template.doctrine` — core public tesseract-compatible template
- `profiles/` — DoctrineOS profile examples
- `doctrineos/` — DoctrineOS prototype shell and runtime
- `sdk/` — Python SDK
- `nodes/` — public concept nodes
- `registry/` — generated public node registry
- `examples/` — adapter and workflow examples
- `tools/` — validation and helper tools
- `tests/` — SDK, example, and DoctrineOS tests
- `docs/` — additional DoctrineOS docs

## Development

```bash
pip install -e . pytest
python -m pytest
python tools/validate_nodes.py
python tools/check_registry.py
```

## License

Licensed under the GNU Affero General Public License v3.0 or later. See [LICENSE](LICENSE) and [NOTICE].

Copyright 2026 Xxaion Labs (Salvatore Anziano / @XxaionLabs)

When using or forking, please retain attribution and link back to this repository.
