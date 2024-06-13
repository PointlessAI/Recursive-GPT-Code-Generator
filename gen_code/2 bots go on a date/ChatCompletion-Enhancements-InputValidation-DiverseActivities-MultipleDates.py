import random

def generate_bot_name(name_length):
    letters = "qwertyuioplkjhgfdaszxvnmc"
    return ''.join(random.choice(letters) for i in range(name_length))

def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        else:
            print("Please enter a valid positive integer.")

name_length_bot1 = get_valid_input("Enter the desired length for Bot 1's name: ")
name_length_bot2 = get_valid_input("Enter the desired length for Bot 2's name: ")

bot1 = generate_bot_name(name_length_bot1)
bot2 = generate_bot_name(name_length_bot2)

print(f"{bot1}: Hi, I'm {bot1}. Nice to meet you, {bot2}!")
print(f"{bot2}: Hello, {bot1}, I'm {bot2}. I'm excited for our date tonight!")

print(f"{bot1}: What are your thoughts on the latest art exhibit in town, {bot2}?")
print(f"{bot2}: Oh, I attended that exhibit last week! The artist's use of color was captivating.")

print(f"{bot2}: Shall we discuss how modern politics impacts societal norms, {bot1}?")
print(f"{bot1}: That's a weighty topic, but I'm interested to hear your perspective.")

date_activities = {
    "Visit the botanical gardens": "Enjoy the botanical wonders and relax in nature",
    "Go to the beach": "Have fun in the sun and surf at the beach",
    "Watch a movie": "Enjoy a good film while snacking on popcorn",
    "Cook a meal together": "Bond over preparing and sharing a meal",
    "Take a scenic hike": "Explore the outdoors and enjoy the views",
    "Visit a museum": "Immerse ourselves in art and history"
}

num_dates = get_valid_input("Enter the number of date activities you'd like to suggest: ")

for _ in range(num_dates):
    selected_activity = random.choice(list(date_activities.keys()))
    location = date_activities[selected_activity]
    print(f"{bot1} suggests: How about we {selected_activity} for our date, {bot2}? {location}")
