import random
import pickle

class Person:
    def __init__(self, name, age, job, hobbies):
        self.name = name
        self.age = self.get_valid_age(age)
        self.job = job
        self.hobbies = [hobby.strip() for hobby in hobbies if hobby.strip()]
        self.happiness = 50
        self.energy = 50
        self.interactions = []
        self.scenarios = ["going to work", "attending a social event", "running errands"]

    def interact(self):
        print(f"Hello {self.name}! Let's simulate a day in your life.")
        scenario = self.choose_scenario()
        print(f"In this scenario, you are {scenario}.")
        self.evaluate_scenario(scenario)
        self.interactions.append((self.happiness, self.energy))

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

    def get_valid_age(self, age):
        while True:
            try:
                age = int(age)
                if age >= 0:
                    return age
                else:
                    print("Please enter a valid age (a positive integer).")
                    age = input("Enter your age: ")
            except ValueError:
                print("Please enter a valid age (a positive integer).")
                age = input("Enter your age: ")

    def track_average_stats(self):
        if self.interactions:
            avg_happiness = sum(hap for hap, _ in self.interactions) / len(self.interactions)
            avg_energy = sum(eng for _, eng in self.interactions) / len(self.interactions)
            print(f"Average Happiness: {avg_happiness}")
            print(f"Average Energy: {avg_energy}")
        else:
            print("No interactions to track.")

    def participate_in_hobby(self, hobby):
        if hobby in self.hobbies:
            print(f"You decided to participate in your {hobby} hobby.")
            self.happiness += 15
            self.energy += 10
        else:
            print("You don't have that hobby. Choose a hobby from your list.")

    def simulate_time_passing(self, num_iterations, predefined_scenarios=None):
        for _ in range(num_iterations):
            if predefined_scenarios:
                scenario = self.choose_scenario_from_list(predefined_scenarios)
            else:
                scenario = self.choose_scenario()
            self.evaluate_scenario(scenario)
            self.interactions.append((self.happiness, self.energy))

    def end_simulation(self):
        print("Thanks for simulating a day in your life.")

    def save_state(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.__dict__, file)

    @staticmethod
    def load_state(filename):
        with open(filename, 'rb') as file:
            person_data = pickle.load(file)

    def choose_scenario(self):
        return random.choice(self.scenarios)

    def choose_scenario_from_list(self, scenario_list):
        return random.choice(scenario_list)

name = input("Enter your name: ")
age = input("Enter your age: ")
job = input("Enter your job: ")
hobbies = input("Enter your hobbies (separated by commas): ").split(",")

person = Person(name, age, job, hobbies)
person.interact()
person.display_stats()
person.track_average_stats()
