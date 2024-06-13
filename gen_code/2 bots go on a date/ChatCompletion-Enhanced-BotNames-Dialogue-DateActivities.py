import random

def generate_bot_name(name_length):
    letters = "qwertyuioplkjhgfdaszxvnmc"
    return ''.join(random.choice(letters) for i in range(name_length))

bot1 = generate_bot_name(6)
bot2 = generate_bot_name(5)

print(f"{bot1}: Hi, I'm {bot1}. Nice to meet you, {bot2}!")
print(f"{bot2}: Hello, {bot1}, I'm {bot2}. I'm excited for our date tonight!")

print(f"{bot1}: What are your thoughts on the latest art exhibit in town, {bot2}?")
print(f"{bot2}: Oh, I attended that exhibit last week! The artist's use of color was captivating.")

print(f"{bot2}: Shall we discuss how modern politics impacts societal norms, {bot1}?")
print(f"{bot1}: That's a weighty topic, but I'm interested to hear your perspective.")

date_activities = {
    "Visit the botanical gardens": "Etiquette etiquette itahr ",
    "Go to the beach": "Erkess Brown Southstraction "
}

selected_activity = random.choice(list(date_activities.keys()))
location = date_activities[selected_activity]

print(f"{bot1} suggests: How about we {selected_activity} for our date, {bot2}?")
