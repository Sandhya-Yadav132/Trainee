class Employee:
    def __init__(self, name):
        self._name = name  # The underscore indicates a "private" variable

    @property
    def name(self):
        """The Getter: Runs when you read 'emp.name'"""
        print("Fetching name...")
        return self._name

    @name.setter
    def name(self, value):
        """The Setter: Runs when you assign 'emp.name = value'"""
        if not value:
            raise ValueError("Name cannot be empty!")
        print("Updating name...")
        self._name = value

    @name.deleter
    def name(self):
        """The Deleter: Runs when you execute 'del emp.name'"""
        print("Deleting name...")
        del self._name

emp=Employee('sandhya')

print(emp.name)

emp.name='yadav'

print(emp.name)
