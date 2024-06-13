import re
import random

def validate_input(name, error_message):
    if not bool(re.match("^[a-zA-Z]+$", name)):
        print(error_message)
        return False
    return True

def get_user_suggestion():
    suggestion = input("Enter a custom date idea: ")
    return suggestion

def plan_date(bot1_name, bot2_name):
    # Add your implementation for planning a date here
    return "Watch a movie together"

def get_date_rating():
    # Implement a more diverse rating system here
    return random.randint(1, 10)

def bot1_generate_comment(selected_idea, bot_name):
    # Implement unique comments for bot 1 based on selected idea
    return f"Bot 1 thinks {selected_idea} is a great choice!"

def bot2_generate_comment(selected_idea, bot_name):
    # Implement unique comments for bot 2 based on selected idea
    return f"Bot 2 is excited about {selected_idea}!"

def display_date_outcome(selected_idea, date_rating, bot1_name, bot2_name, bot1_comment, bot2_comment):
    print("Date Outcome:")
    print(f"Idea selected: {selected_idea}")
    print(f"Date rating: {date_rating}")
    print(f"Comments from {bot1_name}: {bot1_comment}")
    print(f"Comments from {bot2_name}: {bot2_comment}")

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

    bot1_comment = bot1_generate_comment(selected_idea, bot1_name)
    bot2_comment = bot2_generate_comment(selected_idea, bot2_name)

    display_date_outcome(selected_idea, date_rating, bot1_name, bot2_name, bot1_comment, bot2_comment)
