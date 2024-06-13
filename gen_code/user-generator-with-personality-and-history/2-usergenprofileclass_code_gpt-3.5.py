import random

class UserGenerator:
    def __init__(self):
        self.names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        self.personalities = ['friendly', 'creative', 'analytical', 'calm', 'confident']
        self.history = {}

    def generate_user(self):
        name = random.choice(self.names)
        personality = random.choice(self.personalities)
        self.history.setdefault(name, []).append(personality)
        return name, personality

    def get_user_profile(self, name):
        if name in self.history:
            return f"{name} has the following personalities: {', '.join(self.history[name])}"
        else:
            return f"No history available for {name}"

    def get_personality_count(self, personality):
        count = sum(personality in personalities for personalities in self.history.values())
        return f"The personality '{personality}' appears {count} times in the history."

# Demo the code
user_gen = UserGenerator()

for _ in range(5):  # Demo to generate more users
    user_gen.generate_user()

print("User History:")
for user, personalities in user_gen.history.items():
    for personality in personalities:
        print(f"{user} is {personality}")

print(user_gen.get_user_profile('Alice'))
print(user_gen.get_personality_count('friendly'))
