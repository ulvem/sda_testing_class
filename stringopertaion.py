class StringOperation:
    """
    - Constructor accept a string _init_
        Methods
        - Get length of string
        - Reverse the string
        - if length > 5: get the first three characters
        - if length > 6: get the last 4 characters
        - Accept int for a user that is less than length of the string and return the character in position [int]
        Test
        Write test all your methods
        Repository
        Push to gitlab/github
        If any error, attempt to google at least 3 times for solutions 

    """
    def __init__(self, userstr) -> None:
        self.__userstr = userstr

    def reverse_string(self):
        return self.__userstr[::-1]

    def __get_length_of_string(self):
        return len(self.__userstr)

    def get_length(self):
        return self.__get_length_of_string()

    def first_three_characters(self):
        if self.__get_length_of_string() > 5:
            return self.__userstr[0:3]
        else:
            return None

    def last_four_characters(self):
        if self.__get_length_of_string() > 6:
            return self.__userstr[-4:]

        else:
            return None

    def get_positional_character(self, position:int = 0) -> str:
        if not isinstance(position, int):
            raise TypeError("position must be string")

        if position < self.__get_length_of_string():
            return self.__userstr[position]

        else:
            return None


value = StringOperation("My name is Oyindolapo")
print(f"{value.get_length()}")
print(f"{value.reverse_string()}")
print(f"{value.last_four_characters()}")
print(f"{value.first_three_characters()}")
print(f"{value.get_postional_character(4)}")
