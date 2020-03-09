# OOP Basics

This repo will contain our OOP basics

We will look at:
- Abstraction
- Inheritance
- Polymorphism
- Encapsulation


# Class
- Is like a cookie cutter that creates instances of cookies
- They are wrappers to define how an object looks and behaves
- Classes will wrap characteristics as attributes and behaviours as methods


# Method vs Functions
- Methods are functions that belong to a specific data type
- Where functions are aynonymous and anything can call and run them
- Where as **methods need the instance to be called**


# Characteristics / How an object looks like
- There are attributes that are assigned to each instance
- They are variables assigned to an object/instance


# Instance
Occurrence of something


# Self
- Refers to the instance on which a method is being called 

```python
self.name = 'ringo'
```
This means that specific object attribute name will have the string 'ringo'


# Abstraction
- The ability to hide complexity
- We do this using:
    - Seperation of concerns
    - Documentation
        - Specify which methods and how to use them
    - Inheritance
- Inheritance causes some level of abstraction
    
- Real life examples are everywhere:
    - Changing gears
    - Heating up food with one button
    - Using our cards to pass security

# Encapsulation
Making methods or attributes **private**
- To make something private is to **restrict access** from external functions/methods
- When methods or attributes are private, they can only be called by its own functions or within a class

This leads to getters and setters

Example:


# Inheritance
- The ability to pass to child class all the methods and characteristics
- This is one of the big reasons for OOP - it means you can reuse code

**Promise of reusable code**
- You do this by passing the parent class as an argument of the child class
```python
class Animal():
    pass

class Reptile(Animal):
    pass
``` 

# Polymorphism
- Literally means many forms
- Basically, it is the ability to **completely override methods**, and if need be, recall methods from parent class using .super()



# .super()
It represents the parent class, allows you to call methods from parent class.

Usage and case in point:
- Situation where you want to overwrite a method (say method.honk() or make a .sound())
- You want to add new functionality to the new method but still have everything from the first method
- Then you call super()

- Most of the time, this happnes with the __init__ method
    - You want to add new characteristics to child objects
    - And you want to keep all the original characteristics
    - So you override the init method and still call the original init method, with all the necessary arguments

Example:
```python
class Animal():
    # Original init method with age and colour_fur
    def __init__(self, age, colour_fur):
        self.age = age
        self.colour_fur = colour_fur

class Reptile(Animal):
    # this overrides the original init method
    # however what we want is to keep all the original code and add more code
    def __init__(self, name, age, colour_f):
        # use super to call original init method
        # we need to pass the arguments for the original init to work
        super().__init__(age, colour_f) 
        self.name = name

rt = Reptile('Ringo', 10, 'Shiny Gold')
```
