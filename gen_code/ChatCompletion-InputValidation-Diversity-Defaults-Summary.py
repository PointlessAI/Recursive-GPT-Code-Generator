import random

class Person:
    def __init__(self, name=None, age=None, gender=None, hair_color=None, eye_color=None, height=None):
        self.name = name if name else random.choice(['John Doe', 'Jane Doe'])
        self.age = age if 0 <= age <= 120 else random.randint(18, 60)
        self.gender = gender if gender in ["Male", "Female"] else random.choice(["Male", "Female"])
        self.hair_color = hair_color if hair_color in ["Black", "Brown", "Blonde", "Red", "Gray"] else random.choice(["Black", "Brown", "Blonde", "Red", "Gray"])
        self.eye_color = eye_color if eye_color in ["Brown", "Blue", "Green", "Hazel"] else random.choice(["Brown", "Blue", "Green", "Hazel"])
        self.height = height if 150 <= height <= 200 else random.randint(150, 200)

def generate_person(name=None, age=None, gender=None, hair_color=None, eye_color=None, height=None):
    return Person(name, age, gender, hair_color, eye_color, height)
