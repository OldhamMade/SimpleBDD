try:
    import unittest2 as unittest
except ImportError:
    import unittest


class SimpleSpec(unittest.TestCase):
    # this will be collected by nose
    def it_should_pass(self):
        assert True


class BasicSpec:
    # this will be collected by pytest
    def it_should_pass(self):
        assert True


# This will be collected by both nose and pytest
def ensure_pass():
    assert True
