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
        life_expectancy_factors = {
            "adventurous": -5,
            "serious": 3,
            # Add more traits and factors as needed
        }
        prediction = base_life_expectancy
        for trait in self.traits:
            if trait in life_expectancy_factors:
                prediction += life_expectancy_factors[trait]
        return prediction

    def print_summary(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

def generate_random_person(names=["Alice", "Bob", "Charlie", "David", "Eve"], traits=["kind", "funny", "serious", "adventurous", "creative"], num_traits=3):
    name = random.choice(names)
    age = random.randint(18, 60)
    gender = random.choice(["Male", "Female"])
    traits = random.sample(traits, num_traits)
    return Person(name, age, gender, traits)

# Test the code by generating a random person
random_person = generate_random_person()
print(random_person)
random_person_traits = random_person.traits
print(f"Predicted Life Expectancy: {random_person.predicted_life_expectancy()} years")
print(random_person.print_summary())
