class Person:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    
    def print_name(self):
        print(self.fname, self.lname)

# x=Person("John", "Doe")
# x.print_name()

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationn_year=year

    def welcome(self):
        print(f"Welcome {self.fname}")

x=Student("Mike", "Olsen", 2019)
print(x.graduationn_year)
x.welcome()
