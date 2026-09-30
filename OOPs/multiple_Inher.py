# class Class1:
#     def m(self):
#         print('1')
#         print("In Class1") 
      
# class Class2(Class1):
#     def m(self):
#         print('2')
#         super().m()
#         print("In Class2")
        

# class Class3(Class1):
#     def m(self):
#         print('3')
#         super().m()
#         print("In Class3")  
       
# class Class4(Class2, Class3):
#        def m(self):
#            print("4")
#            super().m()
#            print("In Class4")
    
# obj = Class4()
# obj.m()
# print(Class4.__mro__)
# print(Class4.mro())

class A:
    def show(self):
        print('A')

class B(A):
    def show(self):
        print('B')

class C(B):
    def show(self):
        print('C')

class D(B,C):
    pass

d = D()
d.show()