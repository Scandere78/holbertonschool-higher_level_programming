#!/usr/bin/env python3
import pickle


class CustomObject:
    """
    Initialize class CustomObject
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display object's attributes
        """
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"is_student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object to a file
        """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file
        """
        with open(filename, 'rb') as f:
            return pickle.load(f)
