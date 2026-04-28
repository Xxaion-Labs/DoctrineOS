# Compatibility

DoctrineOS compatibility begins with Doctrine Protocol compatibility.

A project is `.doctrine compatible` when it can use the public `.doctrine` format and mount doctrine or concept nodes without requiring custom closed extensions.

## Minimum requirements

A compatible tool can:

- load `.doctrine` files or concept nodes
- parse metadata and section headings
- validate required node structure
- produce mounted instruction context
- preserve stable IDs and source paths when available
- keep mount receipts inspectable

## Badge language

Projects may say:

```text
.doctrine compatible
```

when they support the minimum requirements above.

## DoctrineOS ecosystem fit

Compatible projects can act as:

- model adapters
- editor integrations
- local scripts
- services
- workflow runners
- node registries
- OS-level components

The compatibility floor stays intentionally simple so builders can fork, inspect, implement, and improve it.
