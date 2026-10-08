import pickle

class CustomObject:
    """ class to  serialize and deserialize custom Python objects using the pickle"""

    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs_Student: {self.is_student}")

    def serialize(self, filename: str):
        """Serializes the current instance to a binary file."""
        try:
            with open(filename, mode='wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None
            

    @classmethod
    def deserialize(cls, filename: str):
        """Restores and returns the pickled object instance."""
        try:
            with open(filename, mode='rb') as file:
                obj = pickle.load(file)
                return obj


        except Exception:
            return None

if __name__=="__main__":
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize the object
    obj.serialize("object.pkl")

    # Deserialize the object into a new instance
    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    new_obj.display()