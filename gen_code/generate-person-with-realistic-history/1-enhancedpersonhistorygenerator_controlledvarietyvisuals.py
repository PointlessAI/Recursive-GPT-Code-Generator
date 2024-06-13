import random

class Person:
    def __init__(self, name, age, profession, location):
        self.name = name
        self.age = age
        self.profession = profession
        self.location = location
        self.history = []

    def add_event_to_history(self, event):
        self.history.append(event)

def generate_person_history():
    name = "John Doe"
    age = random.randint(20, 80)
    profession = random.choice(["doctor", "teacher", "engineer", "artist"])
    location = random.choice(["New York", "London", "Paris", "Tokyo"])

    person = Person(name, age, profession, location)

    events = [
        "Graduated from university",
        "Got married",
        "Had children",
        "Started own business",
        "Traveled the world",
        "Fought in a war",
        "Survived a natural disaster"
    ]

    for _ in range(random.randint(3, 7)):
        event = random.choice(events)
        person.add_event_to_history(event)

    return person

person = generate_person_history()

print(f"Name: {person.name}")
print(f"Age: {person.age}")
print(f"Profession: {person.profession}")
print(f"Location: {person.location}")
print("History:")
for i, event in enumerate(person.history, 1):
    print(f"{i}. {event}")
