#!/usr/bin/python3
"""
Write a class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
"""


class Student:
    """write a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function retrieves a dictionary representation of a Student
        """
        if attrs is None or not isinstance(attrs, (list)):
            return vars(self)
        else:
            ret = {k: v for k, v in filter(lambda x: x[0] in attrs,
                                           self.__dict__.items())}
            return ret
