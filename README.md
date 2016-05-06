# Simple BDD

Behaviour-driven-development doesn't have to be complicated. Using the example in this repository, you can
get started writing simple BDD tests in Python in `snake_case` format, collected either using
    [nose](https://nose.readthedocs.io) or [pytest](http://pytest.org).

## Example

Using the provided `setup.cfg` file, tests names can be written using the following prefixes:

* `ensure_*`
* `it_*`
* `must_*`
* `should_*`

eg.:

    def ensure_one_does_not_equal_two():
        assert 1 != 2

These tests can be grouped into classes with the following suffixes:

* `*Spec`
* `*Specs`
* `*Example`
* `*Examples`

eg.:

    class SimpleSpec(unittest.TestCase):
        def it_should_always_fail(self):
            assert True is False

Tests are collected from files with the following suffixes:

* `*_spec.py`
* `*_specs.py`
* `*_example.py`
* `*_examples.py`

To illustrate this, a file has been provied in the `specs` directory named `simple_spec.py`.

## Notes

### [nose](https://nose.readthedocs.io)

When using [nose](https://nose.readthedocs.io), test classes **must** extend from
`unittest.TestCase`, otherwise they won't be collected correctly.

It's recommended to use [figleaf]() and [pinocchio]() with the following options enabled in
`setup.cfg`, which will provide a more BDD-friendly output:

    [nosetests]
    ...
    with-spec=1
    spec-color=1

### [pytest](http://pytest.org)

When using [pytest](http://pytest.org), test classes which use the above formatting rules
**should not** extend from `unittest.TestCase`, since pytest will ignore these expecting them
to be collected using the unittest module's default loader.
