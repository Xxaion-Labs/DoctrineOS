# Prototype Shell

The Soul Protocol prototype shell is the first runnable operating surface for the public compatibility runtime.

It is small on purpose. Before a system becomes vast, its spine must be visible.

## What the shell proves

The shell proves that a readable control object can become runtime context without giving the machine hidden authority.

```text
profile -> mount -> command -> capability -> approval -> adapter -> receipt -> state
```

That is the first living circuit of the public prototype.

## Use

The shell can:

- load a compatibility profile
- mount the profile into instruction context
- emit mount-aware receipts
- accept user direction
- identify required capabilities
- request approval before permissioned action
- route approved actions to safe adapters
- record state
- refuse unapproved actions

## Commands

Start the interactive shell:

```bash
doctrineos
```

Print boot status as JSON:

```bash
doctrineos --json
```

Run one command:

```bash
doctrineos inspect workspace
```

Approve a permissioned command for scripts or tests:

```bash
doctrineos --yes inspect workspace
```

## State and receipts

Runtime state is currently written under the compatibility state directory.

Action receipts are written under the compatibility receipts directory.

Receipts are the public trail. They do not make broad claims. They record the narrow truth of what the runtime mounted, requested, approved, routed, or changed.

## Boundary

This prototype is intentionally small, inspectable, and safe by default. It is a proof spine, not a finished operating world.
