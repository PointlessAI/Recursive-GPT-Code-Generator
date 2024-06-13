import random

class Person:
    def __init__(self, name=None, age=None, gender=None, hair_color=None, eye_color=None, height=None, profession=None):
        self.name = name if name else random.choice(['John Doe', 'Jane Doe'])
        self.age = age if 0 <= age <= 120 else random.randint(18, 60)
        self.gender = gender if gender in ["Male", "Female"] else random.choice(["Male", "Female"])
        self.hair_color = hair_color if hair_color in ["Black", "Brown", "Blonde", "Red", "Gray"] else random.choice(["Black", "Brown", "Blonde", "Red", "Gray"])
        self.eye_color = eye_color if eye_color in ["Brown", "Blue", "Green", "Hazel"] else random.choice(["Brown", "Blue", "Green", "Hazel"])
        self.height = height if 100 <= height <= 250 else random.randint(100, 250)
        self.profession = profession if profession else random.choice(['Doctor', 'Teacher', 'Engineer', 'Artist'])

    def body_mass_index(self, weight):
        return weight / ((self.height / 100) ** 2)

    def increase_age(self, years):
        self.age += years

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Hair Color: {self.hair_color}")
        print(f"Eye Color: {self.eye_color}")
        print(f"Height: {self.height}")
        if hasattr(self, 'profession'):
            print(f"Profession: {self.profession}")

    def validate_age_for_profession(self):
        valid_age_ranges = {
            'Doctor': (30, 70),
            'Teacher': (22, 65),
            'Engineer': (25, 75),
            'Artist': (20, 60)
        }
        if self.profession in valid_age_ranges:
            min_age, max_age = valid_age_ranges[self.profession]
            if not (min_age <= self.age <= max_age):
                print(f"Warning: Age {self.age} is not suitable for the profession {self.profession}.")

    @staticmethod
    def validate_input(value, valid_list):
        return value if value in valid_list else None

    @classmethod
    def generate_random_person(cls, professions=None):
        if professions is None:
            professions = ['Doctor', 'Teacher', 'Engineer', 'Artist']
        name = random.choice(['John Doe', 'Jane Doe'])
        age = random.randint(18, 60)
        gender = random.choice(["Male", "Female"])
        hair_color = random.choice(["Black", "Brown", "Blonde", "Red", "Gray"])
        eye_color = random.choice(["Brown", "Blue", "Green", "Hazel"])
        height = random.randint(100, 250)
        profession = random.choice(professions)
        person = cls(name, age, gender, hair_color, eye_color, height, profession)
        person.validate_age_for_profession()
        return person

    def update_attributes(self, attributes):
        for attr_name, value in attributes.items():
            if hasattr(self, attr_name):
                setattr(self, attr_name, value)

# Example usage:
person1 = Person.generate_random_person()
person1.print_details()
person1.increase_age(5)
person1.print_details()
print(f"Body Mass Index: {person1.body_mass_index(70)}")
person1.update_attributes({'age': 25, 'hair_color': 'Blonde'})
person1.print_details()