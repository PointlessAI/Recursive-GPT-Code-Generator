import random

class Person:
    def __init__(self, name, age, job, hobbies):
        self.name = name
        self.age = age
        self.job = job
        self.hobbies = hobbies
        self.happiness = 50
        self.energy = 50

    def interact(self):
        print(f"Hello {self.name}! Let's simulate a day in your life.")
        scenario = generate_scenario()
        print(f"In this scenario, you are {scenario}.")
        self.evaluate_scenario(scenario)

    def evaluate_scenario(self, scenario):
        if "work" in scenario:
            self.happiness -= 10
            self.energy -= 20
        elif "social event" in scenario:
            self.happiness += 20
            self.energy -= 10
        elif "running errands" in scenario:
            self.energy -= 15

    def display_stats(self):
        print(f"{self.name}'s current stats:")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")

def generate_scenario():
    scenarios = ["going to work", "attending a social event", "running errands"]
    return random.choice(scenarios)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
job = input("Enter your job: ")
hobbies = input("Enter your hobbies (separated by commas): ").split(",")

person = Person(name, age, job, hobbies)
person.interact()
person.display_stats()
