import random
import datetime

class Person:
    def __init__(self, name, age, profession, location):
        self.name = name
        self.age = age
        self.profession = profession
        self.location = location
        self.history = []

    def add_event_to_history(self, event, date):
        self.history.append((event, date))

    def display_full_history(self):
        print(f"History of {self.name}:")
        for i, (event, date) in enumerate(self.history, 1):
            print(f"{i}. {date.strftime('%Y-%m-%d')}: {event}")

        if not self.history:
            print("No events in the history.")

    def generate_realistic_event(self):
        positive_events = [
            "Received a promotion",
            "Published a book",
            "Started a successful business",
            "Won an award",
            "Bought a house",
            "Traveled to a dream destination"
        ]

        negative_events = [
            "Experienced a medical emergency",
            "Survived a car crash",
            "Lost a job",
            "Faced a financial crisis",
            "Went through a divorce",
            "Encountered a natural disaster"
        ]

        event_type = random.choice(["positive", "negative"])
        if event_type == "positive":
            event = random.choice(positive_events)
        else:
            event = random.choice(negative_events)

        # Generating a random date within the last 10 years
        current_year = datetime.datetime.now().year
        event_year = random.randint(current_year - 10, current_year)
        event_month = random.randint(1, 12)
        event_day = random.randint(1, 28)  # Assuming maximum of 28 days in a month
        event_date = datetime.datetime(event_year, event_month, event_day)

        return event, event_date

def generate_person_history_with_events():
    name = input("Enter the person's name: ")
    age = random.randint(20, 80)
    profession = random.choice(["doctor", "teacher", "engineer", "artist"])
    location = random.choice(["New York", "London", "Paris", "Tokyo"])

    person = Person(name, age, profession, location)

    for _ in range(random.randint(3, 7)):
        event, event_date = person.generate_realistic_event()
        person.add_event_to_history(event, event_date)

    return person

person = generate_person_history_with_events()

print(f"Name: {person.name}")
print(f"Age: {person.age}")
print(f"Profession: {person.profession}")
print(f"Location: {person.location}")
print("History:")
person.display_full_history()
