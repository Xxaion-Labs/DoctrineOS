# Compatibility

Soul Protocol compatibility begins with support for `.soul` objects.

The current implementation also supports the `.doctrine` compatibility surface during transition.

## Minimum requirements

A compatible tool can:

- load `.soul`, `.doctrine`, or concept node files
- parse metadata and section headings
- parse JSON sentinel blocks when present
- report sentinel parse errors instead of silently ignoring them
- validate required node structure
- produce mounted instruction context
- preserve stable IDs and source paths when available
- keep mount receipts inspectable

## Badge language

Projects may say `.soul compatible` when they support the forward public filetype trajectory.

Projects may say `.doctrine compatible` when they specifically support the current compatibility surface.

## Ecosystem fit

Compatible projects can act as model adapters, editor integrations, local scripts, services, workflow runners, node registries, and system components.

The compatibility floor stays intentionally simple so builders can fork, inspect, implement, and improve it.

## Boundary

Compatibility does not imply unsupported capability claims. Implementations should keep authority, permission, receipts, and user control explicit.
