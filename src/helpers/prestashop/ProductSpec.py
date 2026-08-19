from dataclasses import dataclass, field


@dataclass(frozen=True)
class ProductSpec:
    name: str
    attributes: dict[str, str] = field(default_factory=dict)