def assert_equals(expected, actual):
    _assert_equals(expected, actual)

    if type(expected) == list:
        if len(expected) != len(actual):
            raise Exception(f"Expected list length {len(expected)} but found {len(actual)}")
        else:
            for i in range(len(expected)):
                _assert_equals(expected[i], actual[i])


def _assert_equals(expected, actual):
    expected_type = type(expected)
    actual_type = type(actual)

    if expected_type != actual_type:
        raise Exception(f"Expected type {expected_type.__name__} but found type {actual_type.__name__}")
    if expected_type == str:
        if expected != actual:
            raise Exception(f"Expected \"{expected}\" but found \"{actual}\"")
    elif expected_type == int:
        if expected != actual:
            raise Exception(f"Expected {expected} but found {actual}")
