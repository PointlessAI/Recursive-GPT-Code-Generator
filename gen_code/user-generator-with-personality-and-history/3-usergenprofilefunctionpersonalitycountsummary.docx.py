import random

class UserGenerator:
    def __init__(self):
        self.names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        self.personalities = ['friendly', 'creative', 'analytical', 'calm', 'confident']
        self.history = {}

    def generate_user(self):
        name = random.choice(self.names)
        personality = random.choice(self.personalities)
        traits = [random.choice(self.personalities) for _ in range(3)]
        self.history.setdefault(name, []).append((personality, traits))
        return name, personality

    def get_user_profile(self, name):
        if name in self.history:
            personality, traits = self.history[name][0]
            return f"{name} has a {personality} personality with Traits: {', '.join(traits)}"
        else:
            return f"No details available for {name}"

    def get_personality_count(self, personality):
        count = sum(personality in all_personalities for _, all_personalities in self.history.values())
        return f"The personality '{personality}' appears {count} times in the history."

user_gen = UserGenerator()

for _ in range(5):
    user_gen.generate_user()

print("User History:")
for user, data in user_gen.history.items():
    personality, traits = data[0]
    print(f"{user} has a {personality} personality with Traits: {', '.join(traits)}")

print(user_gen.get_user_profile('Alice'))
print(user_gen.get_personality_count('friendly'))
