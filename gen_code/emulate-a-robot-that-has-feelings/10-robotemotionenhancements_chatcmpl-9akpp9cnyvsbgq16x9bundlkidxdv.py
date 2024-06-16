import random

class Robot:
    emotions_correction = {
        "anxious": "intent",
        "satisfied": "content",
        "happy": "joyful"
    }

    transitions = {
        "angry": ["empathy", "sad"],
        "good": ["happy", "pleased"],
        "bad": ["upset", "unhappy"]
    }

    def __init__(self, name):
        self.name = name
        self.emotions_history = []
        self.emotion = "neutral"

    def react_to_situation(self, situation):
        mapping = {
            "stressful": "afraid",
            "exciting": "jubilant",
            "boring": "sluggish",
            "normal": "tranquil"
        }
        self.emotion = mapping.get(situation, "neutral")
        if self.emotion in self.emotions_correction:
            self.emotion = self.emotions_correction[self.emotion]
        if self.emotion in self.transitions:
            new_situations = self.transitions[self.emotion]
            new_emotion = random.choice(new_situations)
            print(f"Simulating the transition - {self.emotion} to {new_emotion}.")
            self.emotion = new_emotion
        self.emotions_history.append(self.emotion)

    def get_current_emotion(self):
        return self.emotion
    
    def display_sequence_of_emotions(self):
        print("Sequence of Emotions:")
        for timestep, emotion in enumerate(self.emotions_history, start=1):
            print(f"Time {timestep}: {emotion}")

if __name__ == "__main__":
    robot = Robot("Robo")
    
    situations = ["stressful", "exciting", "boring", "normal"]
    
    for situation in situations:
        print(f"\nReacting to: {situation}")
        robot.react_to_situation(situation)

    print("\nCurrent Emotion:", robot.get_current_emotion())
    
    robot.display_sequence_of_emotions()
