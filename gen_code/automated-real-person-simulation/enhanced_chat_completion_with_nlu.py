import pyttsx3
import speech_recognition as sr
import spacy

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
            sentiment = doc.cats['emotion']
            return sentiment
        except:
            return "neutral"
        
    def respond(self, user_input):
        emotion = self.analyze_emotion(user_input)
        
        if emotion == 'happy':
            response = "I'm glad to hear that!"
        elif emotion == 'frustrated':
            response = "I understand your frustration."
        elif emotion == 'sad':
            response = "I'm here for you."
        else:
            response = "Interesting..."
        
        self.text_to_speech(response)
        return response
