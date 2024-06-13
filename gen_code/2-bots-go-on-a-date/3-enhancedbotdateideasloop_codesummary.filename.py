while True:
    bot1_name = input("Enter the name of the first bot: ")
    bot2_name = input("Enter the name of the second bot: ")

    import random

    date_ideas = [
        f"Watch a movie {bot1_name} wanted to see",
        f"Have a picnic in {bot2_name}'s favorite park",
        "Go on a long drive and listen to music",
        "Try cooking a new meal together",
        "Play mini-golf as a fun date idea"
    ]

    selected_idea = random.choice(date_ideas)

    print(f"{bot1_name} and {bot2_name} decide to {selected_idea} on their date")

    date_rating = int(input("Rate the date from 1 to 10: "))
    print(f"The user rating for the date is: {date_rating}/10")

    date_went_well = random.choice([True, False])

    if date_went_well:
        print(f"The date went well! {bot1_name} and {bot2_name} had a great time.")
        good_dates = {'date_idea': selected_idea, 'rating': date_rating}
    else:
        print(f"Unfortunately, the date didn't go as planned. {bot1_name} and {bot2_name} didn't have as much fun.")
        bad_dates = {'date_idea': selected_idea, 'rating': date_rating}
