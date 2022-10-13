class Employee:
    def __init__(self, name, empid):
        self.name = name
        self.empid = empid

    def greet(self):
        print()

emp1 = Employee("Arjun",78923)

print("employee name ",emp1.name)
print("employee name ",emp1.empid)
emp1.greet()


emp2 = Employee('Anu', 126554)
