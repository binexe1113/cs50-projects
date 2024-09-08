import pytest

from seasons import transform_min
from seasons import transform_read
from seasons import is_ok

def test1():
    with pytest.raises(ValueError):
        is_ok("januray-01-10")
        


