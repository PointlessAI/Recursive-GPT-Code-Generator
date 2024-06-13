import random

class UserGenerator:
    def __init__(self):
        self.names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        self.personalities = ['friendly', 'creative', 'analytical', 'calm', 'confident']
        self.personality_history = {personality: [] for personality in self.personalities}
        self.user_history = {}

    def generate_user(self):
        name = random.choice(self.names)
        personality = random.choice(self.personalities)
        traits = [random.choice(self.personalities) for _ in range(3)]
        self.user_history.setdefault(name, []).append((personality, traits))
        self.personality_history[personality].append(name)
        return name, personality

    def get_user_profile(self, name):
        if name in self.user_history:
            su = 's' if len(self.user_history[name]) > 1 else ''
            personality, traits = self.user_history[name][0]
            return f"{name} has a {personality} personality with Traits: {', '.join(traits)}. They have been generated {len(self.user_history[name])} time{su}."
        else:
            return f"No details available for {name}"

user_gen = UserGenerator()

for _ in range(5):
    user_gen.generate_user()

print("User History:")
for user, data in user_gen.user_history.items():
    personality, traits = data[0]
    print(f"{user} has a {personality} personality with Traits: {', '.join(traits)}")

print(user_gen.get_user_profile('Alice'))

