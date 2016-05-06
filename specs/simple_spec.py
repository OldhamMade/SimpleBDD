try:
    import unittest2 as unittest
except ImportError:
    import unittest


class SimpleSpec(unittest.TestCase):
    """SimpleSpec: this will be picked up by Nose"""
    def it_should_pass(self):
        assert True


class BasicSpec:
    """BasicSpec: this will be picked up by pytest"""
    def it_should_pass(self):
        assert True


def ensure_pass():
    assert True
