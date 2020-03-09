# Define our animal class

# Sudo code:
# Looks / characteristics of every animal
    # name, age, colour heart, brain

# Behaviours / Methods of every animal
    # Eat, sleep, reproduce, potty, make_sound


class Animal():
    # define behaviours and characteristics
    def __init__(self, name, age_days, colour="green"):

    # define the characteristics of every animal
        self.name = name
        self.__age_days = age_days
        self.colour = colour
        self.heart = True
        self.brain = True
        self.skills = {}

        # age
        # we should be able to retrieve the age
        # we should not be able to change/alter the age
            # a user should not be able to set his/her own age
            # however, as the animal sleeps, it should increment the age

        # first let's make the age private
        # create a method that gets the age and returns it
    def get_age(self): # a getter method - allows access to encapsulated resources
        return self.__age_days # inside the class, we have access to the private methods


        # change the sleep method to increment age
    def set_age(self, age_days = 500):
        self.__age_days = age_days
        # we should not be able to change/alter the age without being admin

        # fake verification
        password = input('Password please')

        if password == 'SuperSecret':
            self.__age_days = age_days
            return True
        else:
            return False


    def __increment_age(self):
        self.__age_days += 1


    # defining the method .eat(), .sleep(). .reproduce(), .potty(), .make_sound()
    def eat(self):
        # when it eats, it should increment the age
        # we will do this by calling the  __increment_age() method
        return 'Nom nom nom'

    def sleep(self):
        # increment days in age by 1
        self.__increment_age()
        return 'zzzZzZZzZZZz'

    def reproduce(self):
        return 'Need some privacy'

    def potty(self):
        return 'About to let last night\'s food out'

    def make_sound(self):
        return 'woof'

# To call methods, we need an object of this class
# creating an instance of class animal

ringo = Animal('Ringo', 44, 'Green') #creates instance of class animal and assigns to variable ringo
# checking and printing the instance

print(ringo.get_age())
print(ringo.set_age(500))
print(ringo.get_age())


# calling methods on instance of animal
print(ringo.eat())
print(ringo.potty())
print(ringo.sleep())

# Check the attribute of an instance
print(ringo.name, ringo.get_age())


# second animal
mini = Animal('John', 92, 'Pink')
print(mini.name, mini.get_age(), mini.sleep())
