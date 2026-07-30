from pathlib import Path

SNAPSHOT_DIR = (
    Path(__file__).parent.parent.parent
    / "resources"
    / "snapshots"
)


def load_snapshot(
    name: str,
    locale: str | None = None,
    namespace: str | None = None,
) -> str:
    directory = SNAPSHOT_DIR / namespace if namespace else SNAPSHOT_DIR
    filename = f"{name}_{locale}.yml" if locale else f"{name}.yml"
    path = directory / filename
    return path.read_text(encoding="utf-8")