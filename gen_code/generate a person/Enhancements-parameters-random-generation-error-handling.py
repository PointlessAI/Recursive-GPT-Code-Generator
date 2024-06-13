import random

class Person:
    def __init__(self, name=None, age=None, gender=None, hair_color=None, eye_color=None, height=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.height = height
        
def generate_person(name=None, age=None, gender=None, hair_color=None, eye_color=None, height=None):
    if name is None:
        name = "Unknown"
    if age is None:
        age = random.randint(18, 60)
    if gender is None:
        gender = random.choice(["Male", "Female"])
    if hair_color is None:
        hair_color = random.choice(["Black", "Brown", "Blonde", "Red", "Gray"])
    if eye_color is None:
        eye_color = random.choice(["Brown", "Blue", "Green", "Hazel"])
    if height is None:
        height = random.randint(150, 200)
        
    return Person(name, age, gender, hair_color, eye_color, height)
