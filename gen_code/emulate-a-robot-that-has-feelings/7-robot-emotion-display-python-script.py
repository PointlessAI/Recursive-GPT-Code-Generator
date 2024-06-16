import random
import time

class Robot:
    def __init__(self, name):
        self.name = name
        self.emotion = "neutral"
    
    def react_to_situation(self, situation):
        mapping = {
            "stressful": "anxious",
            "exciting": "happy",
            "boring": "bored",
            "normal": "neutral"
        }
        self.emotion = mapping.get(situation, "neutral")
        self.display_emotion()

    def add_pauses(self):
        pauses = [0.5, 1, 1.5, 2]
        time.sleep(random.choice(pauses))

    def display_emotion(self):
        print(f"{self.name} feels {self.emotion}.")
        self.add_pauses()

# Example usage with the enhancements
if __name__ == "__main__":
    robot = Robot("Robo")
    
    situations = ["stressful", "exciting", "boring", "normal"]
    
    for situation in situations:
        print(f"\nReacting to: {situation}")
        robot.react_to_situation(situation)
