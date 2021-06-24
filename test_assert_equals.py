import pytest

from assert_equals import assert_equals


def test_no_error_string():
    assert_equals("abc", "abc")


def test_error_string():
    with pytest.raises(Exception, match="Expected \"abcef\" but found \"abc\""):
        assert_equals("abcef", "abc")


def test_no_error_integer():
    assert_equals(1, 1)


def test_error_integer():
    with pytest.raises(Exception, match="Expected 1 but found 2"):
        assert_equals(1, 2)


def test_error_type_coercion():
    with pytest.raises(Exception, match="Expected type int but found type str"):
        assert_equals(1, '1')


def test_no_error_list():
    assert_equals(["a", "b", "c"], ["a", "b", "c"])


def test_error_list_length():
    with pytest.raises(Exception, match="Expected list length 2 but found 3"):
        assert_equals(["a", "b"], ["a", "b", "c"])


def test_error_list_items_string():
    with pytest.raises(Exception, match="Expected \"b\" but found \"d\""):
        assert_equals(["a", "b"], ["a", "d"])


def test_error_list_items_int():
    with pytest.raises(Exception, match="Expected 2 but found 3"):
        assert_equals([1, 2], [1, 3])


def test_error_list_items_length():
    with pytest.raises(Exception, match="Expected list length 2 but found 3"):
        assert_equals([[1, 2], [3, 4]], [[1, 2, 3], [3, 4]])


def test_error_list_items_list_int():
    with pytest.raises(Exception, match="Expected 4 but found 5"):
        assert_equals([[1, 2], [3, 4]], [[1, 2], [3, 5]])


def test_error_list_items_list_string():
    with pytest.raises(Exception, match="Expected \"d\" but found \"e\""):
        assert_equals([["a", "b"], ["c", "d"]], [["a", "b"], ["c", "e"]])
