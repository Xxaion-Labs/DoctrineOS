# ⧉ Soul Protocol

[![Validate Soul Protocol](https://github.com/Xxaion-Labs/Soul-Protocol/actions/workflows/validate.yml/badge.svg)](https://github.com/Xxaion-Labs/Soul-Protocol/actions/workflows/validate.yml)

**Soul Protocol is an open, AGPL-licensed control grammar for AI-native computing: a way to turn readable meaning into mountable runtime structure while keeping human authority, proof, and permission visible.**

Version: 0.1.0 Prototype  
License: AGPLv3-or-later

```text
.soul

    (digital)
A                Soul Protocol object

 ⧉
```

The symbol is the object.

In prose, call it **a Soul Protocol object**.

A Soul Protocol object is a semantic-machine vessel: readable by humans, structured for machines, mountable by runtimes, bounded by receipts, and designed to preserve useful context instead of letting it vanish after every prompt.

## The idea

Most AI software still treats intelligence like a product window. You type into a box, context is temporarily assembled, a model answers, and much of the achieved structure evaporates.

Soul Protocol points at a different operating shape.

```text
meaning -> object -> mount -> capability -> permission -> action -> receipt -> state
```

The goal is not to make AI mysterious. The goal is to make powerful AI behavior **legible**.

Soul Protocol asks:

- What if important context could be stored as readable control matter?
- What if behavior could be mounted instead of improvised?
- What if every powerful action had a capability boundary and a receipt?
- What if the user remained the root authority while machines gained better structure to act within?

## How it works

Soul Protocol uses plain, inspectable artifacts as control surfaces.

1. A file or node carries meaning in human-readable form.
2. Structured metadata and sections make that meaning machine-readable.
3. A mount operation converts the object into runtime context.
4. The runtime identifies needed capabilities before acting.
5. The user approves permissioned actions.
6. The adapter performs only the approved action.
7. A receipt records what happened.
8. State remains inspectable and recoverable.

This is the core spine:

```text
Soul Protocol object
  -> mount receipt
  -> instruction context
  -> capability check
  -> permission gate
  -> adapter call
  -> action receipt
  -> runtime state
```

## What this repo contains

Soul Protocol currently includes:

- public `.soul` object standard documentation
- `.doctrine` compatibility loading, parsing, validation, and mounting
- SDK and CLI support for the compatibility layer
- mount receipts with context hashes
- public concept nodes and generated node registry
- adapter examples
- prototype shell for the current compatibility runtime
- default compatibility profile
- action receipts and runtime state logging
- GitHub Actions validation

`.doctrine` remains the current compatibility surface during transition. `.soul` is the forward public trajectory.

## Why it matters

Soul Protocol is trying to replace disposable prompt matter with reusable control matter.

It gives builders a public floor for:

- mountable context
- explicit authority
- capability-scoped actions
- inspectable receipts
- reusable behavior nodes
- open protocol experimentation
- user-governed AI runtimes

The mythic part is not decoration. The mythic part is the shape: a readable object that becomes a runtime surface without becoming a black box.

## Quick start

```bash
git clone https://github.com/Xxaion-Labs/Soul-Protocol.git
cd Soul-Protocol
pip install -e .
```

Mount the standard public compatibility file:

```bash
doctrine mount standard_public_template.doctrine
```

Run the prototype shell:

```bash
doctrineos --json
doctrineos inspect workspace
doctrineos --yes inspect workspace
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

- [⧉](SOUL_PROTOCOL.md) — public `.soul` / Soul Protocol object standard
- [How it works](docs/how-it-works.md) — full operating explanation
- [Vision](VISION.md) — why Soul Protocol exists
- [Architecture](ARCHITECTURE.md) — system layers and control spine
- [Specification](SPEC.md) — `.soul`, `.doctrine` compatibility, mounting, validation, and receipts
- [Compatibility](COMPATIBILITY.md) — public compatibility requirements
- [Roadmap](ROADMAP.md) — build path from prototype to public operating environment
- [Prototype Shell](docs/prototype-shell.md) — runnable shell guide
- [Examples](examples/README.md) — adapter and workflow examples
- [Nodes](nodes/README.md) — public concept node library
- [Changelog](CHANGELOG.md) — release history
- [Contributing](CONTRIBUTING.md) — contribution guide

## Repository structure

- `SOUL_PROTOCOL.md` — public `.soul` / `⧉` standard
- `standard_public_template.doctrine` — core public compatibility template
- `profiles/` — compatibility profile examples
- `doctrineos/` — prototype shell and runtime
- `sdk/` — Python SDK
- `nodes/` — public concept nodes
- `registry/` — generated public node registry
- `examples/` — adapter and workflow examples
- `tools/` — validation and helper tools
- `tests/` — SDK, example, and shell tests
- `docs/` — additional Soul Protocol docs

## Boundary

Soul Protocol does not claim that AI systems gain personhood, independent authority, or unsupported capabilities. It is a public protocol and prototype for making AI behavior more structured, inspectable, permissioned, and user-governed.

## License

Licensed under the GNU Affero General Public License v3.0 or later. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

Copyright 2026 Xxaion Labs (Salvatore Anziano / @XxaionLabs)

When using or forking, please retain attribution and link back to this repository.
