# Examples

These examples show the first practical moves of Soul Protocol: mount context, carry it into another system, and preserve enough metadata for the work to remain traceable.

They are intentionally small. Each example demonstrates one link in the chain.

```text
object -> mount -> context -> adapter payload
```

## Prompt context export

```bash
python examples/prompt_context_export.py
```

Writes mounted instruction context to `mounted_context.txt`.

Use this when you want to see the raw context that a mount produces before handing it to another tool.

## API payload adapter

```bash
python examples/api_payload_adapter.py
```

Builds a generic payload with mounted context, user message, stable ID, and context hash metadata.

Use this to understand how mounted control matter can travel into model-facing systems without losing its source identity.

## Local model prompt

```bash
python examples/local_model_prompt.py
```

Builds a plain-text prompt for local model workflows.

Use this when the target runtime is simple and expects text rather than a structured API payload.

## Testing

The example scripts are covered by `tests/test_examples.py` so they do not silently drift.

## Principle

Examples should remain readable, boring in execution, and powerful in implication. The alien shape belongs in the architecture; the implementation should be easy to inspect.
