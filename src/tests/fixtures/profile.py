import pytest

@pytest.fixture
def profile(request):
    return request.param