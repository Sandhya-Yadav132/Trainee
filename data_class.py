# from dataclasses import dataclass

# @dataclass
# class UserProfile:
#     username: str
#     email: str
#     role: str = 'guest'
#     is_active: bool = True


# user1 = UserProfile(username="sandhya", email="sandhya@123")
# print(user1)

# user2 = UserProfile(username="ram", email="ram@123", role="admin")
# print(user2.role)


# from dataclasses import dataclass

# @dataclass(frozen=True)
# class Point3D:
#     x: float
#     y: float
#     z: float

# origin = Point3D(0.0, 0.0, 0.0)

# # Trying to modify a value will raise an error
# try:
#     origin.x = 5.0
# except AttributeError as e:
#     print(f"Error: {e}")
#     # Output: Error: cannot assign to field 'x'

# # Because it is frozen, it is hashable and can be a dictionary key
# locations = {origin: "Center of the map"}
# print(locations[origin])
# # Output: Center of the map


# from dataclasses import dataclass, field

# @dataclass
# class Book:
#     title: str
#     author: str
#     pages: int
#     price: float
#     discount_percentage: float = 0.0
    
#     # This field will be calculated automatically, so we don't pass it to __init__
#     final_price: float = field(init=False)

#     def __post_init__(self):
#         # 1. Validation
#         if self.pages <= 0:
#             raise ValueError("A book must have at least 1 page!")
        
#         # 2. Calculation
#         discount_amount = self.price * (self.discount_percentage / 100)
#         self.final_price = self.price - discount_amount

# # Creating a valid book
# book = Book(title="Python Tricks", author="Dan Bader", pages=300, price=29.99, discount_percentage=10)
# print(f"Final Price: ${book.final_price:.2f}")
# # Output: Final Price: $26.99

# # Triggering the validation error
# try:
#     invalid_book = Book(title="Empty Ghost", author="None", pages=0, price=5.00)
# except ValueError as e:
#     print(f"Validation Failed: {e}")
#     # Output: Validation Failed: A book must have at least 1 page!



from dataclasses import dataclass


#Test frozen=True: Create an employee instance and try to change their name (e.g., emp1.empname = 'New Name'). 
# Watch how Python completely blocks it and throws an error!
@dataclass(frozen=False, order=True)
class Employee:

    empname: str
    email:str
    age: int
    role: str
    salary: float = 0.0

emp1 = Employee(empname='sandhya', email='sandhya@123',age=22, role='python developer')

emp2 = Employee(empname='ram', email='ram@123', salary=50000, age=24, role='react developer')

emp3 = Employee(empname='kanha', email='ram@123', salary=50000, age=23, role='developer')


emp1.empname = 'akshay'

emp1.hobby = 'cricket'

# s = sorted([emp1,emp2, emp3])

print(emp1)
# # print(emp2)

# # print(s)


# from dataclasses import dataclass, field

# @dataclass
# class Employee:
#     empname: str
#     age: int
#     role: str
#     salary: float = 0.0
    
#     # init=False tells Python: "Do not ask the user for this in the constructor"
#     email: str = field(init=False)

#     def __post_init__(self):
#         # 1. DATA VALIDATION
#         # If someone passes an invalid age, we block the object from being created
#         if self.age < 18:
#             raise ValueError(f"Employee must be at least 18 years old! Got: {self.age}")
        
#         # 2. DERIVED MATH / CALCULATIONS
#         # We automatically format a professional email using their name
#         clean_name = self.empname.lower().replace(" ", "")
#         self.email = f"{clean_name}@company.com"

# emp1 = Employee(empname="Sandhya", age=16, role="Python Developer")

# # Notice we didn't pass an email, but Python calculated it perfectly!
# print(emp1.email)
# # Output: sandhya@company.com
# print(emp1)
# # Output: Employee(empname='Sandhya', age=22, role='Python Developer', salary=0.0, email='sandhya@company.com')
