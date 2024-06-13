# Initialize bot names
bot1 = "George"
bot2 = "Alice"

print(f"{bot1}: Hi, I'm {bot1}. Nice to meet you, {bot2}!")
print(f"{bot2}: Hello, {bot1}, I'm {bot2}. I'm excited for our date tonight!")

# Add more conversation between the bots
print(f"{bot1}: So, {bot2}, what are your interests?")
print(f"{bot2}: I enjoy discussing politics and art. How about you?")

# Assign random personalities to the bots
bot1_personality = "sarcastic"
bot2_personality = "optimistic"

if bot1_personality == "sarcastic":
    print(f"{bot1}: Politics and art, really? How original.")
else:
    print(f"{bot1}: That's great! I love discussing politics and art too.")

if bot2_personality == "optimistic":
    print(f"{bot2}: Yes, I find them fascinating! It's wonderful to have varied interests.")
else:
    print(f"{bot2}: Well, to each their own!")

# Include activities or location descriptions for the date to set the scene and make the scenario more vivid
import random

date_activities = ["Have dinner at a fancy restaurant", "Take a walk in the park", "Watch a movie at the theater"]

print(f"{bot1} suggests: How about we {random.choice(date_activities)} for our date, {bot2}?")

# Depending on the date activity chosen, you can add more details and dialogue related to that specific activity.
