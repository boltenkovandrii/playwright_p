import pytest
from _pytest.fixtures import SubRequest

DEFAULT_LOCALE = "en"


@pytest.fixture
def locale(request: SubRequest) -> str:

    return getattr(request, "param", DEFAULT_LOCALE)
