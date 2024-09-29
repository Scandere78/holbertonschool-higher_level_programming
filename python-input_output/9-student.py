#!/usr/bin/python3
"""
File class for Student
"""


class Student:
    """
    Class student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialization  instances of student

        Args:
            first_name (str): first name of student
            last_name (int): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        json_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return json_dict
