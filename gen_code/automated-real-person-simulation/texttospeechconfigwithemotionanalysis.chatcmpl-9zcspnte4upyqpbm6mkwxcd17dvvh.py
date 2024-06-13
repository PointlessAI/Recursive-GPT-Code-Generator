import pyttsx3
import speech_recognition as sr
import spacy
from textblob import TextBlob
from textblob import Blobber
from textblob.en import sentiment as pattern_sentiment

class AutomatedRealPersonSimulation:
    def __init__(self, language="en", voice="english"):
        self.nlp = spacy.load("en_core_web_sm")
        self.language = language
        self.voice = voice
        
    def text_to_speech(self, text):
        engine = pyttsx3.init()
        try:
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 0.9)
            engine.setProperty('voice', self.voice)
            engine.say(text)
            engine.runAndWait()
        except pyttsx3.engine.UnknownValueError:
            raise InvalidTextError("Text cannot be read by the engine.")
        
    def analyze_emotion(self, user_input):
        emotions = {
            "joy": 0.0,
            "sadness": 0.0,
            "anger": 0.0,
            "surprise": 0.0,
            "fear": 0.0
        }
        doc = self.nlp(user_input)
        for token in doc:
            if token.text.lower() in emotions:
                emotions[token.text.lower()] += 1
        
        return emotions
        
    def respond(self, user_input):
        emotions = self.analyze_emotion(user_input)
        
        max_emotion = max(emotions, key=emotions.get)
        
        response = f"The predominant emotion detected is {max_emotion}."
        
        self.text_to_speech(response)
        return response
