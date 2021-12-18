import pytest
import sys

def test_add_numbers():
    assert 10 + 2 == 12

def test_sum_of_elements_in_a_list():
    numbers = [12, 23, 1, 45, 7]
    expected = 88
    sum_of_numbers = sum(numbers)
    assert sum_of_numbers == expected

@pytest.mark.xfail
def test_if_capital():
    name = "Oyin"
    assert name.isupper()

@pytest.mark.xfail(sys.platform == "win32", reason="Doesnt work on windows")
def test_fail_when_os_is_win():
    assert True

@pytest.mark.auth
def test_my_marker_works():
    assert True

@pytest.mark.database
def test_my_marker_works_database():
    assert True