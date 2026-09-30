def master_function(pos1, pos2, /, normal, *args, kw_only, **kwargs):
    print("Positional-Only:", pos1, pos2)
    print("Normal:", normal)
    print("Args:", args)
    print("Keyword-Only:", kw_only)
    print("Kwargs:", kwargs)

# इस फंक्शन को परफेक्ट तरीके से कॉल करने का तरीका:
# master_function(1, 2,3, 4, 5, 6, kw_only="Compulsory Name", city="Delhi", age=25)

# master_function(1, 2, 4, 5, 6, normal=3,kw_only="Compulsory Name", city="Delhi", age=25)


# master_function(1, 2, 3, kw_only="Compulsory Name",)

# 1. positional only - required
# 2. normal - required
# 3. args = optional
# 4. keyword -only - required
# 5. kwargs = optional

# def func(a,b,d,c=20): # positional argument sbse phle aate h then sare keyword or default arguments
#     print(d)
#     print(c)
# func(1,2,3,8)

def fun(a,/):
    print(a)

# fun(5)
# fun(a=5)   #TypeError: fun() got some positional-only arguments passed as keyword arguments: 'a'

def fun1(*,a):
    print(a)

# fun1(a=5)
# fun1(5)     #TypeError: fun1() takes 0 positional arguments but 1 was given