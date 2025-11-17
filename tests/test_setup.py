import selenium
import pytest

def test_environment_setup():
    assert selenium.__version__