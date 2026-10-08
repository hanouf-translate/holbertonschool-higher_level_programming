import pickle
class CustomObjects():
    """ class to  serialize and deserialize custom Python objects using the pickle"""

    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs_Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance to a binary file."""
        try:
            with open(filename, mode='wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None
            

    @classmethod
    def deserialize(cls, filename):
        """Restores and returns the pickled object instance."""
        try:
            with open(filename, mode='rb') as file:
                obj = pickle.load(filename)
                if isinstance(obj, cls):
                    return obj
                return None

        except Exception:
            retrun None
