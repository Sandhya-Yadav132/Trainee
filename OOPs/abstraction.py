from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def showA(self, a, b):
        print('A')
        # pass

    @abstractmethod
    def showB(self):
        print('B')
        # pass

# a = A()

# a.showA() #TypeError: Can't instantiate abstract class A without an implementation for abstract methods 'showA', 'showB'

class B(A):

    def showA(self):
        print('a')

    def showB(self):
        pass

    def show(self):
        print('Hi')

b = B()

b.showA()