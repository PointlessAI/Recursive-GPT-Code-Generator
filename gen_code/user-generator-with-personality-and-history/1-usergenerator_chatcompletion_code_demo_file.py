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

# Demo the code
user_gen = UserGenerator()
user1 = user_gen.generate_user()
user2 = user_gen.generate_user()
user3 = user_gen.generate_user()

print("User History:")
for user, personalities in user_gen.history.items():
    for personality in personalities:
        print(f"{user} is {personality}")
