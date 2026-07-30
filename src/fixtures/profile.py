import pytest

@pytest.fixture
def profile(request):
    return getattr(request, "param", "desktop")