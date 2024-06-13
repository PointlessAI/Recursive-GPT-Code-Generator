import re
import random

def validate_input(name, error_message):
    if not bool(re.match("^[a-zA-Z]+$", name)):
        print(error_message)
        return False
    return True

def get_user_suggestion():
    suggestion = input("Enter a custom date idea: ").strip()

    while not suggestion:
        print("Invalid input. Please enter a valid suggestion.")
        suggestion = input("Enter a custom date idea: ").strip()

    return suggestion

def plan_date(bot1_name, bot2_name):
    # Actual date planning implementation(complex logic to-be implemented later)
    return "Watch a movie together"

def get_date_rating():
    # More elaborate and comprehensive rating system
    entertainment = random.randint(1, 10)
    return entertainment

# Demo the updated code
while True:
    bot1_name = input("Enter the name of the first bot: ").strip()
    if not validate_input(bot1_name, "Bot name can only contain letters. Please enter a valid name."):
        continue

    bot2_name = input("Enter the name of the second bot: ").strip()
    if not validate_input(bot2_name, "Bot name can only contain letters. Please enter a valid name."):
        continue

    selected_idea = plan_date(bot1_name, bot2_name)
    if not selected_idea:
        user_suggestion = get_user_suggestion()
        selected_idea = user_suggestion

    date_rating = get_date_rating()

    bot1_comment = f"Bot 1 thinks {selected_idea} is a great choice!"
    bot2_comment = f"Bot 2 is excited about {selected_idea}!"

    print("Date Outcome:")
    print(f"Idea selected: {selected_idea}")
    print(f"Date rating: {date_rating}")
    print(f"Comments from {bot1_name}: {bot1_comment}")
    print(f"Comments from {bot2_name}: {bot2_comment}")
