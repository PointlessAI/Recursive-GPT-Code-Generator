bot1_name = input("Enter the name of the first bot: ")
bot2_name = input("Enter the name of the second bot: ")

import random

date_ideas = ["Go to a movie", "Have a picnic", "Take a walk in the park", "Go out for dinner"]

selected_idea = random.choice(date_ideas)

print(f"{bot1_name} and {bot2_name} decide to {selected_idea} on their date")

date_went_well = random.choice([True, False])

if date_went_well:
    print(f"The date went well! {bot1_name} and {bot2_name} had a great time.")
else:
    print(f"Unfortunately, the date didn't go as planned. {bot1_name} and {bot2_name} didn't have as much fun.")
