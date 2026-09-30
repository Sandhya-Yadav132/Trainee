# class int:
#     pass


# m = int()
# print(str(m))
# print(repr(m))


# class meta:
#     def __str__(self):
#         return "Hello Meta"

#     def __repr__(self):
#         return f"class meta with pass"

# m1 = meta()
# print(m1)
# print([m1])

# from datetime import datetime

# now = datetime(2026, 9, 17, 14, 30, 0)

# print(str(now))   # Output: 2026-09-17 14:30:00
# print(repr(now))  # Output: datetime.datetime(2026, 9, 17, 14, 30, 0)


user = 'sandhya\n@🤔'

print(str(user))
print(f"{user}")
print(f"{user!s}")

print(repr(user))
print(f"{user!r}")
# print(repr(user!r)) # throw error

print(f"{user!a}")    #'sandhya\n@\U0001f914'


# 1. Define variables with special characters and hidden actions
# text_data = "Café\n"
# number_data = 100

# print("--- 1. USING TEXT DATA ('Café\\n') ---")
# # !s (Default) -> Executes the \n (creates a real empty line)
# print(f"Human Lens  (!s): {text_data!s}")

# # !r (Developer) -> Keeps it literal, adds single quotes, shows \n
# print(f"Dev Lens    (!r): {text_data!r}")

# # !a (ASCII Safe) -> Converts 'é' to unicode escape character
# print(f"Safe Lens   (!a): {text_data!a}")


# print("\n--- 2. USING NUMBER DATA (100) ---")
# # For numbers, all three flags look identical because numbers 
# # don't have hidden formatting quotes or special accents.
# print(f"Human Lens  (!s): {number_data!s}")
# print(f"Dev Lens    (!r): {number_data!r}")
# print(f"Safe Lens   (!a): {number_data!a}")


# print("\n--- 3. SHORTCUT vs FUNCTION EQUIVALENTS ---")
# # Proving that the f-string flag is just a cleaner shortcut
# print(f"Shortcut (!r):    {text_data!r}")
# print(f"Function (repr):  {repr(text_data)}")
