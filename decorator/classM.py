class A:
   
    def hello1():
        print('hi1')

    @classmethod
    def hello2(cls):
        print('hi2')

A.hello1()
A.hello2()

obj=A()
# obj.hello1()
obj.hello2()
A().hello2()