#Beginner Level

#Create a class Animal with attributes species and sound. Define a method make_sound to print the
#sound. Then, create subclasses Dog and Cat that inherit from Animal and set different sounds.
#Instantiate these objects and call their methods.
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} goes '{self.sound}'")


class Dog(Animal):
    def __init__(self):
        super().__init__(species="Dog", sound="Woof")


class Cat(Animal):
    def __init__(self):
        super().__init__(species="Cat", sound="Meow")


dog = Dog()
cat = Cat()


dog.make_sound()  
cat.make_sound()  


#Using Inheritance and the Super() Function
#Create a base class Person with attributes name and age, and a method display_info. Create a
#subclass Employee that inherits from Person and adds an attribute salary. Use super() in the
#Employee class to initialize the base class’s attributes. Create objects and display their information.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def display_info(self):
        super().display_info()
        print(f"Salary: {self.salary}")


person = Person("Ahmed", 21)
employee = Employee("Hassan", 30, 20000)
person.display_info()
employee.display_info()


#Basic Polymorphism with Classes
#Create a class Vehicle with a method start_engine that prints "Engine started." Create two subclasses
#Car and Boat, each with its own version of start_engine. Demonstrate polymorphism by calling
#start_engine from objects of Car and Boat.

class Vehicle:
    def start_engine(self):
        print("Engine started.")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with a roar!")

class Boat(Vehicle):
    def start_engine(self):
        print("Boat engine started with a smooth hum!")

vehicle = Vehicle()
car = Car()
boat = Boat()

vehicle.start_engine()  
car.start_engine()      
boat.start_engine()    



#intermidiate level
#Class Polymorphism in Action
#Create a base class Media with a method play. Then, create subclasses Audio and Video, each with a
#different implementation of the play method. Write a function that accepts an object of type Media
#and calls its play method, demonstrating polymorphism.


class media:
    def play(self):
        print('media has been played')

class video(media):
    def play(self):
        print('video has been played')

class audio(media):
    def play(self):
        print('audio has been played')

def func(media_object):
    media_object.play()

media_file=media()
audio_file=audio()
video_file=video()

func(media_file)
func(audio_file)
func(video_file)


#Inheritance and Method Overriding with Super
#Create a class Building with a method build that prints "Building foundation." Create a subclass
#House that overrides build to print "Building a house," but also calls the parent class’s build method
#using super(). Instantiate a House object and call its build method.

class Building:
    def build(self):
        print('Building foundation.')
class House(Building):
    def build(self):
        super().build()
        print('Building a house')

my_building=Building()

my_house=House()

my_building.build()

my_house.build()