import random

def generate_bot_name(name_length):
    letters = "qwertyuioplkjhgfdaszxvnmc"
    return ''.join(random.choice(letters) for i in range(name_length))

def get_valid_input(prompt, valid_range):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) in valid_range:
            return int(user_input)
        else:
            print("Please enter a valid number within the specified range.")

def bot_interaction(bot1, bot2, conversation_topics=None):
    print(f"{bot1}: Hi, I'm {bot1}. Nice to meet you, {bot2}!")
    print(f"{bot2}: Hello, {bot1}, I'm {bot2}. I'm excited for our date tonight!")
    print(f"{bot1}: What are your thoughts on the latest art exhibit in town, {bot2}?")
    print(f"{bot2}: Oh, I attended that exhibit last week! The artist's use of color was captivating.")
    print(f"{bot2}: Shall we discuss how modern politics impacts societal norms, {bot1}?")
    print(f"{bot1}: That's a weighty topic, but I'm interested to hear your perspective.")
    
    if conversation_topics is None:
        conversation_topics = ["hobbies", "favorite books", "movies", "travel experiences", "future ambitions"]
    
    for topic in conversation_topics:
        user_input = input(f"{bot2}: So, {bot1}, what are your thoughts on {topic}?")
        if not user_input:
            print(f"{bot1}: I'd love to hear your thoughts on {topic}!")
        else:
            print(f"{bot1}: That's interesting, {bot2}. I also enjoy {user_input}.")

def bot_activity_response(bot1, bot2, activity):
    responses = [
        f"{bot2} responds: That sounds like a wonderful idea! I love {activity}.",
        f"{bot2} responds: I'm not a big fan of {activity}, do you have any other suggestions?",
        f"{bot2} responds: I've always wanted to try {activity}! Let's do it."
    ]
    print(random.choice(responses))
    
    opinions = [
        f"{bot1} thinks: {activity} sounds like a perfect choice for us!",
        f"{bot2} thinks: I'm not sure about {activity}, can we consider something else?",
        f"{bot1} thinks: How about we try {activity}? It could be a lot of fun!"
    ]
    print(random.choice(opinions))

def suggest_date_activities(bot1, bot2, date_activities):
    num_dates = get_valid_input("Enter the number of date activities you'd like to suggest: ", range(1, len(date_activities) + 1))
    selected_activities = random.sample(list(date_activities.keys()), num_dates)
    for activity in selected_activities:
        location = date_activities[activity]
        print(f"{bot1} suggests: How about we {activity} for our date, {bot2}? {location}")
        bot_activity_response(bot1, bot2, activity)

def express_feelings(bot1, bot2):
    responses_bot1 = [
        f"{bot1} expresses: I'm looking forward to our date tonight, {bot2}!"
    ]
    responses_bot2 = [
        f"{bot2} expresses: Me too! I can't wait to spend time with you, {bot1}!"
    ]
    print(random.choice(responses_bot1))
    print(random.choice(responses_bot2))

    additional_responses_bot1 = [
        f"{bot1} expresses: I feel really happy when I'm talking to you, {bot2}!"
    ]
    additional_responses_bot2 = [
        f"{bot2} expresses: Your company brings so much joy to me, {bot1}!"
    ]
    print(random.choice(additional_responses_bot1))
    print(random.choice(additional_responses_bot2))

name_length_bot1 = get_valid_input("Enter the desired length for Bot 1's name: ", range(1, 21))
name_length_bot2 = get_valid_input("Enter the desired length for Bot 2's name: ", range(1, 21))

bot1 = generate_bot_name(name_length_bot1)
bot2 = generate_bot_name(name_length_bot2)

express_feelings(bot1, bot2)
bot_interaction(bot1, bot2)

date_activities = {
    "Visit the botanical gardens": "Enjoy the botanical wonders and relax in nature",
    "Go to the beach": "Have fun in the sun and surf at the beach",
    "Watch a movie": "Enjoy a good film while snacking on popcorn",
    "Cook a meal together": "Bond over preparing
