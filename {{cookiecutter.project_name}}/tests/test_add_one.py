from {{cookiecutter.project_name}}.add_one import add_one


def test_add_one():
    """
    Test that the add_one function works correctly.
    """
    assert add_one(31) == 32