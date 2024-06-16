class Robot:
    emotions_correction = {
        "anxious": "intent",
        "satisfied": "content"
    }

    transitions = {
        "angry": ["empathy", "sad"],
        "good": ["happy", "pleased"],
        "bad": ["upset", "unhappy"]
    }

    def __init__(self, name):
        self.name = name
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

if __name__ == "__main__":
    robot = Robot("Robo")
    
    situations = ["stressful", "exciting", "boring", "normal"]
    
    for situation in situations:
        print(f"\nReacting to: {situation}")
        robot.react_to_situation(situation)
