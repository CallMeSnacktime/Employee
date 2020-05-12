class Employee:
    #class variable
    raiseAmount = 1.04
    num_of_emps=0

    #constructors
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # Increases number of employees for each instance
        Employee.num_of_emps +=1

    # To avoid changing every use to a method a decorator was used
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    # Method for printing emplyoee full names
    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    # Apply pay raise
    def applyRaise(self):
        self.pay = int(self.pay * self.raiseAmount)

    def __repr__(self):
        # Should be something that can be used in code
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullName, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullName)

    # Sets employee raise
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raiseAmount = amount

    # Splits emplyee string information
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Determine if day entered is a weekday
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raiseAmount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees =[]
        else:
            self.employees = employees

    # Add new employee
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # Remove existing employee
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullName())



import datetime

my_date = datetime.date(2016,11,10)
#print(Employee.is_workday(my_date))

emp1 = Employee('Atiba', 'Lashley', 50000)
emp2 = Employee('test','user', 60000)

dev1 = Developer('Tiba', 'Teebz', 70000, "Python")
dev2 = Developer('tester','Tryer', 80000, "Java")


mgr1 = Manager('Mike', 'Jones', 90000, [dev1])

# Example for __len__ use
print(len(emp1))

# Example for __add__ use
print(emp1+emp2)

# Using setter to change 1st and last name with a
emp1.fullName = 'Ezekiel Anthony'
emp2.fullName = 'Joe Shmoe'

# Full name deleter
del emp2.fullName

# Example for __str__ use
print(emp1)
print(emp2)

print(repr(emp1))
print(str(emp1))






