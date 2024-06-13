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
        trait_indices = random.sample(range(len(self.personalities)), 3)
        traits = [self.personalities[i] for i in trait_indices]
        self.user_history.setdefault(name, []).append((personality, traits))
        self.personality_history[personality].append(name)
        return name, personality, traits

    def compute_occurrence_phrase(self, name):
        occurrence = '' if len(self.user_history.get(name, [])) == 1 else 's'
        return occurrence

    def get_trait_string(self, traits):
        return ', '.join(traits)

    def get_user_profile(self, name):
        userData = self.user_history.get(name, [])
        if userData:
            occurrence = self.compute_occurrence_phrase(name)
            personality, traits = userData[0]
            trait_string = self.get_trait_string(traits)
            return f"{name} has a {personality} personality with Traits: {trait_string}. They have been generated {len(userData)} time{occurrence}."
        else:
            return f"No details available for {name}"

# Demo the enhanced code
user_gen = UserGenerator()

for _ in range(5):
    user_gen.generate_user()

print("User History:")
for user, data in user_gen.user_history.items():
    personality, traits = data[0]
    print(f"{user} has a {personality} personality with Traits: {', '.join(traits)}")

print(user_gen.get_user_profile('Alice'))
