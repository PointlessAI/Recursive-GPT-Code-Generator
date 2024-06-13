import random

class Person:
    def __init__(self, name, age, gender, traits):
        self.name = name
        self.age = age
        self.gender = gender
        self.traits = traits

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Traits: {', '.join(self.traits)}"

# Generate random person
def generate_random_person():
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    name = random.choice(names)
    age = random.randint(18, 60)
    gender = random.choice(["Male", "Female"])
    traits = random.sample(["kind", "funny", "serious", "adventurous", "creative"], random.randint(1, 3))
    return Person(name, age, gender, traits)

# Test the code by generating a random person
random_person = generate_random_person()
print(random_person)
