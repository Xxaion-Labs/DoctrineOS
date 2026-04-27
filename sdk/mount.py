import hashlib
import json
from datetime import datetime, timezone


class MountReceipt:
    def __init__(self, name, doctrine_id, source=None, context="", errors=None, metadata=None):
        self.name = name
        self.doctrine_id = doctrine_id
        self.source = source
        self.context = context
        self.errors = errors or []
        self.metadata = metadata or {}
        self.mounted_at = datetime.now(timezone.utc).isoformat()
        self.context_sha256 = hashlib.sha256(context.encode("utf-8")).hexdigest()

    @classmethod
    def from_doctrine(cls, doctrine, errors=None):
        context = doctrine.to_prompt_context()
        return cls(
            name=doctrine.name,
            doctrine_id=doctrine.id,
            source=doctrine.source,
            context=context,
            errors=errors or [],
            metadata=getattr(doctrine, "metadata", {}) or {},
        )

    def to_dict(self):
        return {
            "mounted": True,
            "name": self.name,
            "id": self.doctrine_id,
            "source": self.source,
            "mounted_at": self.mounted_at,
            "context_sha256": self.context_sha256,
            "metadata": self.metadata,
            "errors": list(self.errors),
            "instruction_context": self.context,
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)
