import random

def plan_date(bot1_name, bot2_name):
    date_ideas = [
        f"Watch a movie {bot1_name} wanted to see",
        f"Have a picnic in {bot2_name}'s favorite park",
        "Go on a long drive and listen to music",
        "Try cooking a new meal together",
        "Play mini-golf as a fun date idea"
    ]

    selected_idea = random.choice(date_ideas)

    print(f"{bot1_name} and {bot2_name} decide to {selected_idea} on their date")
    return selected_idea

def get_date_rating():
    return int(input("Rate the date from 1 to 10: "))

def assign_date_outcome(selected_idea, date_rating, bot1_name, bot2_name):
    date_went_well = random.choice([True, False])

    if date_went_well:
        print(f"The date went well! {bot1_name} and {bot2_name} had a great time.")
        return {'date_idea': selected_idea, 'rating': date_rating}
    else:
        print(f"Unfortunately, the date didn't go as planned. {bot1_name} and {bot2_name} didn't have as much fun.")
        return {'date_idea': selected_idea, 'rating': date_rating}

while True:
    bot1_name = input("Enter the name of the first bot: ")
    bot2_name = input("Enter the name of the second bot: ")

    selected_idea = plan_date(bot1_name, bot2_name)
    date_rating = get_date_rating()

    assign_date_outcome(selected_idea, date_rating, bot1_name, bot2_name)
