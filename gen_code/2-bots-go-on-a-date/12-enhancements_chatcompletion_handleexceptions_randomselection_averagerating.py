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
    ideas = {"Cook a meal together": 5, "Watch a movie": 7, "Play a board game": 8}
    selected_idea = random.choice(list(ideas.keys()))
    return selected_idea, ideas[selected_idea]

def get_date_rating():
    try:
        entertainment = random.randint(1, 10)
        return entertainment
    except Exception as e:
        print(f"An error occurred")

# Demo the updated code
while True:
    bot1_name = input("Enter the name of the first bot: ").strip()
    if not validate_input(bot1_name, "Bot name can only contain letters. Please enter a valid name."):
        continue

    bot2_name = input("Enter the name of the second bot: ").strip()
    if not validate_input(bot2_name, "Bot name can only contain letters. Please enter a valid name."):
        continue

    selected_idea, idea_rating = plan_date(bot1_name, bot2_name)
    if not selected_idea:
        user_suggestion = get_user_suggestion()
        selected_idea = user_suggestion

    date_rating = get_date_rating()

    bot1_comment = f"Bot 1 thinks {selected_idea} is a great choice!"
    bot2_comment = f"Bot 2 is excited about {selected_idea}!"

    print("Date Outcome:")
    print(f"Idea selected: {selected_idea}")
    print(f"Idea rating: {idea_rating}")
    print(f"Average date rating: {(date_rating + idea_rating) / 2}")
    print(f"Comments from {bot1_name}: {bot1_comment}")
    print(f"Comments from {bot2_name}: {bot2_comment}")
