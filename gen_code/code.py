import random

class Person:
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, and I work as a {self.occupation}."

class Human(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender, "human")

    def generate_random_person():
        names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Gina", "Henry"]
        name = random.choice(names)
        age = random.randint(20, 40)
        gender = random.choice(["male", "female"])
        return Human(name, age, gender)

# Example Usage
person1 = Human.generate_random_person()
print(person1.introduce())
import random

class Person:
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, and I work as a {self.occupation}."

    @staticmethod
    def generate_random_person():
        names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Gina", "Henry"]
        name = random.choice(names)
        age = random.randint(20, 40)
        gender = random.choice(["male", "female"])
        return Human(name, age, gender)

class Human(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender, "human")

# Example Usage
person1 = Person.generate_random_person()
print(person1.introduce())
import random

class Person:
    def __init__(self, name, age, gender, occupation, birthplace="Earth"):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.birthplace = birthplace

    @property
    def details(self):
        return f"{self.name} details - Age: {self.age}, Gender: {self.gender}, Occupation: {self.occupation}, Birthplace: {self.birthplace}"

    @staticmethod
    def generate_random_person():
        names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Gina", "Henry"]
        occupations = ["developer", "teacher", "doctor", "artist", "engineer"]
        genders = ["male", "female"]
        locations = ["Earth", "Mars", "Jupiter", "Saturn"]
        
        name = random.choice(names)
        age = random.randint(20, 60)
        gender = random.choice(genders)
        occupation = random.choice(occupations)
        birthplace = random.choice(locations)
        
        return Person(name, age, gender, occupation, birthplace)

class Human(Person):
    def __init__(self, name, age, gender, superpower=None):
        super().__init__(name, age, gender, "human")
        self.superpower = superpower

    @property
    def superpower_details(self):
        if self.superpower:
            return f"{self.name} has the superpower of {self.superpower}"
        else:
            return f"{self.name} does not have any superpower"

# Example Usage
person1 = Person.generate_random_person()
person2 = Human("Eve", 25, "female", "telekinesis")

print(person1.details)
print(person2.details)
print(person2.superpower_details)
import random

class Person:
    def __init__(self, name, age, gender, occupation, birthplace="Earth"):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.birthplace = birthplace

    @property
    def details(self):
        return f"{self.name} details - Age: {self.age}, Gender: {self.gender}, Occupation: {self.occupation}, Birthplace: {self.birthplace}"

    @staticmethod
    def generate_random_person():
        names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Gina", "Henry"]
        occupations = ["developer", "teacher", "doctor", "artist", "engineer"]
        genders = ["male", "female"]
        locations = ["Earth", "Mars", "Jupiter", "Saturn"]
        
        name = random.choice(names)
        age = random.randint(20, 60)
        gender = random.choice(genders)
        occupation = random.choice(occupations)
        birthplace = random.choice(locations)
        
        return Person(name, age, gender, occupation, birthplace)

class Human(Person):
    def __init__(self, name, age, gender, superpower=None):
        super().__init__(name, age, gender, "human")
        self.superpower = superpower

    @property
    def superpower_details(self):
        if self.superpower:
            return f"{self.name} has the superpower of {self.superpower}"
        else:
            return f"{self.name} does not have any superpower"

# Example Usage
person1 = Person.generate_random_person()
person2 = Human("Eve", 25, "female", "telekinesis")

print(person1.details)
print(person2.details)
print(person2.superpower_details)
import random

class Person:
    def __init__(self, name, age, gender, occupation, birthplace="Earth"):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.birthplace = birthplace

    @property
    def details(self):
        return f"{self.name} details - Age: {self.age}, Gender: {self.gender}, Occupation: {self.occupation}, Birthplace: {self.birthplace}"

    @staticmethod
    def generate_random_person():
        names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Gina", "Henry"]
        occupations = ["developer", "teacher", "doctor", "artist", "engineer"]
        genders = ["male", "female"]
        locations = ["Earth", "Mars", "Jupiter", "Saturn"]
        
        name = random.choice(names)
        age = random.randint(20, 60)
        gender = random.choice(genders)
        occupation = random.choice(occupations)
        birthplace = random.choice(locations)
        
        return Person(name, age, gender, occupation, birthplace)

class Human(Person):
    def __init__(self, name, age, gender, superpower=None):
      super().__init__(name, age, gender, "human")
      self.superpower = superpower        

    @property
    def superpower_details(self):
        if self.superpower:
            return f"{self.name} has the superpower of {self.superpower}"
        else:
            return f"{self.name} does not have any superpower"


person1 = Person.generate_random_person()
person2 = Human("Eve", 25, "female", "telekinesis")

print(person1.details)
print(person2.details)
print(person2.superpower_details)  
