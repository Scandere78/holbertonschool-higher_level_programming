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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}

        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict

    def reload_from_json(self, json):
        """
        Replaces attributes of Student instance with those in json dict
        setattr() allows for dynamically modifying an object's attributes
        without having to explicitly write out each update,
        making the code flexible and adaptable to different sets of data.
        """
        for key in json:
            val = json[key]
            setattr(self, key, val)
