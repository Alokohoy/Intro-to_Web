class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
      return f'{self.name}, {self.age}'
p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()

# new class with the same properties as person
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()


def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

    class Student(Person):
        def __init__(self, fname, lname, year):
            super().__init__(fname, lname)
            self.graduationyear = year

        def welcome(self):
            print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)




class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()