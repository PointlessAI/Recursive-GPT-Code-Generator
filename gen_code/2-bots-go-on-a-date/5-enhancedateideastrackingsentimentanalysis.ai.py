import random

date_ratings = {}

def plan_date(bot1_name, bot2_name):
    date_ideas = [
        f"Watch a movie {bot1_name} wanted to see",
        f"Have a picnic in {bot2_name}'s favorite park",
        "Go on a long drive and listen to music",
        "Try cooking a new meal together",
        "Play mini-golf as a fun date idea"
    ]

    # Randomly select a date idea
    selected_idea = random.choice(date_ideas)

    print(f"{bot1_name} and {bot2_name} decide to {selected_idea} on their date")
    
    return selected_idea

def get_date_rating():
    return int(input("Rate the date from 1 to 10: "))

def analyze_date_sentiment(date_rating):
    if date_rating >= 7:
        return 'positive'
    elif 4 <= date_rating < 7:
        return 'neutral'
    else:
        return 'negative'

def assign_date_outcome(selected_idea, date_rating, bot1_name, bot2_name):
    date_sentiment = analyze_date_sentiment(date_rating)
    
    # Update date_ratings for each bot
    if bot1_name not in date_ratings:
        date_ratings[bot1_name] = {'total_rating': 0, 'num_interactions': 0}
    if bot2_name not in date_ratings:
        date_ratings[bot2_name] = {'total_rating': 0, 'num_interactions': 0}

    date_ratings[bot1_name]['total_rating'] += date_rating
    date_ratings[bot1_name]['num_interactions'] += 1

    date_ratings[bot2_name]['total_rating'] += date_rating
    date_ratings[bot2_name]['num_interactions'] += 1

    if date_sentiment == 'positive':
        print(f"The date went well! {bot1_name} and {bot2_name} had a great time.")
    else:
        print(f"Unfortunately, the date didn't go as planned. {bot1_name} and {bot2_name} didn't have as much fun.")

while True:
    bot1_name = input("Enter the name of the first bot: ")
    bot2_name = input("Enter the name of the second bot: ")

    selected_idea = plan_date(bot1_name, bot2_name)
    date_rating = get_date_rating()

    assign_date_outcome(selected_idea, date_rating, bot1_name, bot2_name)

