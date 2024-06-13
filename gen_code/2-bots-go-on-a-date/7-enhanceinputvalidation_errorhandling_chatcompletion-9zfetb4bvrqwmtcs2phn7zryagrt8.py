while True:
    bot1_name = input("Enter the name of the first bot: ").strip()
    if not bot1_name:
        print("Bot name cannot be empty. Please enter a valid name.")
        continue

    bot2_name = input("Enter the name of the second bot: ").strip()
    if not bot2_name:
        print("Bot name cannot be empty. Please enter a valid name.")
        continue

    selected_idea = plan_date(bot1_name, bot2_name)
    date_rating = get_date_rating()

    assign_date_outcome(selected_idea, date_rating, bot1_name, bot2_name)
