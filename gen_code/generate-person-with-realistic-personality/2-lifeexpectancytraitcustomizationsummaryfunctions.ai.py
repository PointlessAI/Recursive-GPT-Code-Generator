import random

class Person:
    def __init__(self, name, age, gender, traits):
        self.name = name
        self.age = age
        self.gender = gender
        self.traits = traits

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Traits: {', '.join(self.traits)}"

    def predicted_life_expectancy(self):
        base_life_expectancy = 80
        if "adventurous" in self.traits:
            return base_life_expectancy - 5
        elif "serious" in self.traits:
            return base_life_expectancy + 3
        else:
            return base_life_expectancy

    def print_summary(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

def generate_random_person(num_traits=3):
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    name = random.choice(names)
    age = random.randint(18, 60)
    gender = random.choice(["Male", "Female"])
    traits = random.sample(["kind", "funny", "serious", "adventurous", "creative"], num_traits)
    return Person(name, age, gender, traits)

# Test the code by generating a random person
random_person = generate_random_person()
print(random_person)
random_person_traits = random_person.traits
print(f"Predicted Life Expectancy: {random_person.predicted_life_expectancy()} years")
print(random_person.print_summary())
