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


def sumvalues(first_number, second_number):
    return first_number+second_number


@pytest.mark.parametrize("numbers, expected_value", [("10 +6", 16)])
def test_evaluate_params(numbers, expected_value):
    assert eval(numbers) == expected_value


@pytest.mark.parametrize("name", [("Oyin",), ("Are",)])
def test_name(name):
    for na in name:
        assert isinstance(na, str)

@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    assert x+y > 1

def test_name_length():
    name = "Ivar"
    name_length = len(name)

    assert name_length == 4

@pytest.mark.xfail(reason="On purpose failure")
def test_area_of_a_rec():
    length = 10
    breadth = 8
    area = length * breadth
    assert area == 70


#Rules
# - test_
# - Test pytest "name_of_file"
# - test pytest

#<<expression>> 

# True == Pass
# False == Fails

#"x,y", [(0,2), (1,2), (0,3), (1,3)]
#x = 0, y = 2
#x = 1, y = 2
#x = 0, y = 3
# x = 1, y = 3