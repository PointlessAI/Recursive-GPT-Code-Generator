import re

def validate_input(name):
    return bool(re.match("^[a-zA-Z]+$", name))

def get_user_suggestion():
    suggestion = input("Enter a custom date idea: ")
    return suggestion

def display_date_outcome(selected_idea, date_rating, bot1_name, bot2_name):
    print("Date Outcome:")
    print(f"Idea selected: {selected_idea}")
    print(f"Date rating: {date_rating}")
    print(f"Comments from {bot1_name}: ")
    # Add comments from bot1
    print(f"Comments from {bot2_name}: ")
    # Add comments from bot2

while True:
    bot1_name = input("Enter the name of the first bot: ").strip()
    if not validate_input(bot1_name):
        print("Bot name can only contain letters. Please enter a valid name.")
        continue

    bot2_name = input("Enter the name of the second bot: ").strip()
    if not validate_input(bot2_name):
        print("Bot name can only contain letters. Please enter a valid name.")
        continue

    selected_idea = plan_date(bot1_name, bot2_name)
    if not selected_idea:
        user_suggestion = get_user_suggestion()
        selected_idea = user_suggestion

    date_rating = get_date_rating()

    assign_date_outcome(selected_idea, date_rating, bot1_name, bot2_name)
    
    display_date_outcome(selected_idea, date_rating, bot1_name, bot2_name)
