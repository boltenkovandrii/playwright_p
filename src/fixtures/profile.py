import pytest
from _pytest.fixtures import SubRequest


@pytest.fixture
def profile(request: SubRequest) -> str:
    return getattr(request, "param", "desktop_1920x1200")
