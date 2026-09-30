class A:
   
    def hello1():
        print('hi1')

    def hello2(self):
        print('hi2')

    @staticmethod
    def hello():
        print('hi')

obj=A()
A.hello()        #hi
obj.hello()      #hi
A.hello1()       #hi1
# obj.hello1()   #A.hello1() takes 0 positional arguments but 1 was given
A.hello2('s')    #hi2
# obj.hello2('s')  #A.hello2() takes 1 positional argument but 2 were given