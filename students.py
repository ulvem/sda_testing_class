"""Create a class Students that holds students record and activities
The class must have a constructor
At least 3 methods
Attempt to Write tests for your class
Push your code to git repository
Create a branch called dev and push your code into branch
Ensure you have a gitignore file - gitignore.io
Ensure commit statements are readable
Have a requirements.txt file"""

#name
#course
#GPA

#__variable = private
#variabe = public
#1-5


class Student:
    def __init__(self, name: str = "John Doe", course: str = "Basic Science", gpa: float = 0.00 ) -> None:
        self.__name = name
        self.__course = course
        self.__validate_gpa_is_float(gpa)
        self.__gpa = gpa

    def __validate_gpa_is_float(self, value):
        #check if gpa is numeric, if not numeric raise an error
        if not isinstance(value, (int, float)):
            raise TypeError(f"{value} should be float")

    def __validate_gpa_is_within_limit(self, number):
        if number < 1 or number > 5:
            raise ValueError(f"{number} is not valid gpa")

    def class_of_student_grade(self):
        self.__validate_gpa_is_within_limit(self.__gpa)
        #4-5 = excellent, 3-4 = good, 2-3 = avarage, poor
        if self.__gpa >= 4.5:
            return "Excellent"
        elif self.__gpa >=3.5 and self.__gpa < 4.5:
            return "Good"
        elif self.__gpa >= 2.5 and self.__gpa < 3.5:
            return "Average"
        else:
            return "Try Harder"

    def get_gpa_rank(self):
        return self.class_of_student_grade(self.__gpa)

    def print_something(self):
        print(f"public")

    def __print_anotherthing(self):
        print(f"private")
    

cal = Student(name="Oyin D", course="CIS", gpa=4.5)
cal2 = Student(name="Jaan", course="CS", gpa=4.23)