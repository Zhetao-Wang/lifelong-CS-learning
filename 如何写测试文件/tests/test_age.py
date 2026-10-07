import pytest

from age import is_adult


def test_adult():
    assert is_adult(20) is True


def test_minor():
    assert is_adult(17) is False


def test_exactly_eighteen():
    assert is_adult(18) is True

#下面这写法要着重注意
def test_negative_age():
    with pytest.raises(ValueError):
        is_adult(-1)