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

    visual_emoji = {
        "afraid": "😨",
        "jubilant": "🎉",
        "sluggish": "😒",
        "tranquil": "😌",
        "neutral": "😐",
        "intent": "😌",
        "content": "😊",
        "joyful": "😃",
        "empathy": "🤝",
        "sad": "😢",
        "happy": "🙂",
        "pleased": "🙂"
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
            self.emotion = new_emotion
        self.emotions_history.append(self.emotion)

    def get_current_emotion(self):
        return self.emotion
    
    def display_sequence_of_emotions(self):
        for emotion in self.emotions_history:
            print(self.visual_emoji.get(emotion, "Unknown Emoji"))


robot = Robot("Robo")
situations = ["stressful", "exciting", "boring", "normal"]

for situation in situations:
    robot.react_to_situation(situation)

print("Current Emotion:", robot.get_current_emotion())
robot.display_sequence_of_emotions()
