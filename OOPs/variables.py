# # Within the Python class we can represent data by using variables.  
# # There are 3 types of variables are allowed.  
 
# # 1. Instance Variables (Object Level Variables) 
# # 2. Static Variables (Class Level Variables) 
# # 3. Local variables (Method Level Variables)

# class Student:
#     school = "ABC School"       # Static/Class variable

#     def __init__(self, name, age,school):
#         self.name = name        # Instance variable
#         self.age = age          # Instance variable
#         self.school=school

#     def display(self):
#         school="Excellence"
#         self.school="JIT"
#         message = "Student Details"   # Local variable
#         print(message)
#         print(self.name, self.age,school)


# s1=Student('sandhya',22,'davv')
# s2=Student('muskan',23,'iit')
# print(s1.school)
# s1.display()
# print(s1.school)
# print(s2.school)


# class Counter:
#     def __init__(self):
#         self.count = 0

#     def increment(self):
#         count += 1

# c = Counter()
# c.increment()

# class demo:
#     def __init__(name,self):
#         name.self=self
#         print(self)

# d=demo(5)
# print(d.self)

# class Demo:
#     school = 'hi'
#     def play_game(self):
#         score = 0
        
#         def score_goal():
#             #nonlocal score
#             score += 10
            
#         score_goal()
#         print(f"Final Score: {score}", Demo.school)

# d = Demo()
# d.play_game()
# print(d.school)
# print(Demo.school)


# class UserProfile:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def get_profile(self):
#         return f"User: {username} | Email: {email}"

# player = UserProfile("ShadowNinja", "ninja@email.com")
# print(player.get_profile())



# class Logger:
#     def __init__(self, username, logs=[]): # logs = None
#         self.username = username
#         self.logs = logs
        # if logs is None:
        #     self.logs = []  # Create a brand new list instance here
        # else:
        #     self.logs = logs

#     def log(self, message):
#         self.logs.append(message)

# user1 = Logger("Alice")
# user1.log("Login success")

# user2 = Logger("Bob")          #Logger("Bob",[]) temporally
# user2.log("Password changed")

# print(user1.logs)  # Currently prints: ['Login success', 'Password changed']
# # Expected output: ['Login success']

class Customer:
    def __init__(self, price):
        self.price = price

    def calculate_total(self):
        return self.price

class VIPCustomer(Customer):
    def calculate_total(self):
        # discounted = self.price * 0.8
        self.price = self.price * 0.8
        # The developer wants to use the base total logic on the discounted price
        return super().calculate_total() 

vip = VIPCustomer(100)
print(vip.calculate_total())  # Currently prints: 100
# Expected output: 80.0
