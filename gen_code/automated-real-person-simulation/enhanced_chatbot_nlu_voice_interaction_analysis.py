import pyttsx3
import speech_recognition as sr
import nltk
from textblob import TextBlob
import spacy
from spacy.lang.en import English

class AutomatedRealPersonSimulation:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        
    def text_to_speech(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        
    def analyze_emotion(self, user_input):
        doc = self.nlp(user_input)
        sentiment = doc.cats['emotion']
        if sentiment == 'happy':
            return "happy"
        elif sentiment == 'frustrated':
            return "frustrated"
        elif sentiment == 'sad':
            return "sad"
        else:
            return "neutral"
        
    def respond(self, user_input):
        emotion = self.analyze_emotion(user_input)
        if emotion == "happy":
            response = "I'm glad to hear that!"
        elif emotion == "frustrated":
            response = "I understand your frustration."
        elif emotion == "sad":
            response = "I'm here for you."
        else:
            response = "Interesting..."
        
        self.text_to_speech(response)
        return response
