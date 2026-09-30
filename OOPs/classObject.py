class Person:
    purpose='storage'
    def __init__(self):
            pass

    def greet(self):
          self.purpose='container'
          print('Hi',self.purpose)

# p1=Person()

p1=Person()
p2=Person()
# print(Person().greet())
# Person().greet()
print(p1.purpose)     #storage
p2.greet()            #Hi container
print(p1.purpose)     #storage
print(p2.purpose)     #container



