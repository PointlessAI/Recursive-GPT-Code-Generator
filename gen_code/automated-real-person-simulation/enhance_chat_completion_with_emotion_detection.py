import pyttsx3
import speech_recognition as sr
import spacy
from textblob import TextBlob

class AutomatedRealPersonSimulation:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        
    def text_to_speech(self, text):
        engine = pyttsx3.init()
        try:
            engine.say(text)
            engine.runAndWait()
        except:
            print("Error: Text to speech conversion failed.")
        
    def analyze_emotion(self, user_input):
        try:
            doc = self.nlp(user_input)
            sentiment = TextBlob(user_input).sentiment.polarity
            return sentiment
        except:
            return 0.0
        
    def respond(self, user_input):
        emotion = self.analyze_emotion(user_input)
        
        if emotion > 0.5:
            response = "I'm glad to hear that!"
        elif emotion < -0.5:
            response = "I understand your frustration."
        elif emotion < 0:
            response = "I'm here for you."
        else:
            response = "Interesting..."
        
        self.text_to_speech(response)
        return response

def main():
    ai = AutomatedRealPersonSimulation()
    
    # Example usage of text_to_speech
    text = "Hello, how are you joy?"
    print(f"Input text: {text}")
    ai.text_to_speech(text)
    
    # Example usage of respond function
    response = ai.respond(text)
    print(f"Response: {response}")

if __name__ == "__main__":
    main()
