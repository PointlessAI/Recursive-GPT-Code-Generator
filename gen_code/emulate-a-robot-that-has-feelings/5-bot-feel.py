import random
import time

class Robot:
    def __init__(self, name):
        self.name = name
        self.emotion = "neutral"

    def react_to_situation(self, situation):
        if "stressful" in situation:
            self.emotion = "anxious"
            self.display_emotion()
        elif "exciting" in situation:
            self.emotion = "happy"
            self.display_emotion()
        elif "boring" in situation:
            self.emotion = "bored"
            self.display_emotion()
        else:
            self.emotion = "neutral"
            self.display_emotion()

    def display_emotion(self):
        print(f"{self.name} feels {self.emotion}.")
        time.sleep(2)

# Example usage
if __name__ == "__main__":
    robot = Robot("Robo")
    
    situations = ["It's a stressful day today.",
                  "We're going to have an exciting event tomorrow!",
                  "Today's tasks seem quite boring.",
                  "Normal routine day without much happening."]
    
    for situation in situations:
        print(f"\nReacting to: {situation}")
        robot.react_to_situation(situation)
