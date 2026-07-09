from pathlib import Path

SNAPSHOT_DIR = (
    Path(__file__).parent.parent.parent
    / "resources"
    / "snapshots"
)


def load_snapshot(name: str, locale: str) -> str:
    path = SNAPSHOT_DIR / f"{name}_{locale}.yml"
    return path.read_text(encoding="utf-8")