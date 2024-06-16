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
            "boring": "bored"
        }
        self.emotion = mapping.get(situation, "neutral")
        self.display_emotion()

    def display_emotion(self):
        print(f"{self.name} feels {self.emotion}.")
        time.sleep(2)

# Example usage with the enhancements
if __name__ == "__main__":
    robot = Robot("Robo")
    
    situations = ["stressful", "exciting", "boring", "normal"]
    
    for situation in situations:
        print(f"\nReacting to: {situation}")
        robot.react_to_situation(situation)
