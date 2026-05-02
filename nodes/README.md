# Public Nodes

Soul Protocol nodes are small reusable behavior units for Soul Protocol-compatible runtimes.

A node is a shard of control matter. It should be small enough to inspect, stable enough to reuse, and clear enough to mount without guesswork.

Nodes let the system grow by composition instead of bloat.

## How nodes work

```text
node -> mount -> instruction context -> behavior pressure
```

A node can define a principle, boundary, response style, workflow rule, or safety posture. It can be mounted alone or composed with other compatibility content.

## Node format

A public node should include:

```markdown
# Node: node-name

## Definition
Short definition.

## Usage
How to use the node.

## Example
Minimal example.

## ID
stable-node-id
```

The format is intentionally simple. A node should be readable by a person before it is useful to a runtime.

## Current nodes

- `anti-drift.md` — encourages consistency with the active mounted context
- `clarity.md` — encourages clear, direct, readable responses
- `concise-response.md` — encourages useful responses with minimal unnecessary length
- `example.md` — minimal reusable concept example
- `safety-boundary.md` — keeps safety and lawful boundaries explicit
- `user-authority.md` — keeps user direction central to the interaction

## Registry

The generated registry is stored at `registry/index.json`.

When adding or changing nodes, run:

```bash
python tools/build_registry.py
python tools/check_registry.py
```

## Principle

A good node is not a wall of doctrine. It is a precise control crystal: small surface, clear meaning, reusable effect.
