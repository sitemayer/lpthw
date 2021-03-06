## Animal is-a object(yes, sort of confusing) look at the extra credit

class Animal(object):
    """docstring for Animal"""
    pass

## is-a
class Dog(Animal):
    """docstring for Dog"""
    def __init__(self, name):
        ## has-a
        self.name = name

## is-a
class Cat(Animal):
    """docstring for Cat"""
    def __init__(self, name):
        ## has-a
        self.name = name


## is-a
class Person(Animal):
    """docstring for Person"""
    def __init__(self, name):
        ## has-a
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    def say_hi(self):
        print "hello"

## is-a
class Employee(Person):
    """docstring for Employee"""
    def __init__(self, name, salary):
        ## has-a hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## has-a
        self.salary = salary

## is-a
class Fish(object):
    pass


## is-a
class Salmon(Fish):
    pass

## is-a
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## is-a
satan = Cat("Satan ")

## is-a
mary = Person("Mary")

## has-a
mary.pet = satan

## is-a
frank = Employee("Frank", 120000)

## has-a
frank.pet = rover

## is-a
flipper = Fish()

## is-a
crouse = Salmon()

## is-a
harry = Halibut()

frank.say_hi()
