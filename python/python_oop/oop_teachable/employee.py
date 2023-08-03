import person

class Employee(person.Person):
    def __init__(self, fname, lname, department):
        self.department = department
        super().__init__(fname, lname)
        
    def print(self):
        print(f'department: {self.department}', end='')
        super().print()
