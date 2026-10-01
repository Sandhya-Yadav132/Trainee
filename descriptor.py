class AgeDescriptor:

    def __get__(self, instance, owner):
        print("Getting age")
        return instance._age

    def __set__(self, instance, value):
        print("Setting age")

        if value < 0:
            raise ValueError("Age cannot be negative")

        instance._age = value

class Student:
    age = AgeDescriptor()


s1 = Student()

s1.age = 25

print(s1.age)