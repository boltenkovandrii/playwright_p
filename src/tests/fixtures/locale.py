import pytest


DEFAULT_LOCALE = "en"

@pytest.fixture
def locale(request):

    return getattr(
        request,
        "param",
        DEFAULT_LOCALE
    )