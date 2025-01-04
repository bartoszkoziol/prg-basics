class Student:

    class_year=2024
    num_students=0

    def __init__(self, name, age):
        self.name=name
        self.age=age
        Student.num_students+=1
    
student1=Student("Spongebob", 30)
student2=Student("Patrick", 35)
student3=Student("Squidward", 5)



print(Student.num_students)
print(student1.name)
print(student2.name)

# class Car:
#  def __init__(self, brand, model, year):
#      self.brand = brand  # Object attribute
#      self.model = model  # Object attribute
#      self.year = year    # Object attribute

#  def display_info(self):
#      print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# car1=Car("BMW", "M3", 2024)

# car1.display_info()