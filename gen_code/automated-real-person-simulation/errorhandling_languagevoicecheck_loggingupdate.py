import pyttsx3
import speech_recognition as sr
import spacy
from textblob import TextBlob
from transformers import pipeline
import logging

class InvalidTextError(Exception):
    pass

class AutomatedRealPersonSimulation:
    def __init__(self, language="en", voice="english"):
        supported_languages = ["en"]
        supported_voices = ["english"]
        
        if language not in supported_languages:
            raise ValueError("Invalid language provided. Supported languages: {}".format(", ".join(supported_languages)))
        
        if voice not in supported_voices:
            raise ValueError("Invalid voice provided. Supported voices: {}".format(", ".join(supported_voices)))
        
        self.nlp = spacy.load("en_core_web_sm")
        self.language = language
        self.voice = voice
        self.speech_recognizer = sr.Recognizer()
        self.logger = logging.getLogger("error_logger")
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('error.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        
    def text_to_speech(self, text):
        engine = pyttsx3.init()
        try:
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 0.9)
            engine.setProperty('voice', self.voice)
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            self.logger.error(f"Error in text_to_speech function: {e}")
            raise InvalidTextError("Text-to-speech conversion failed.")
        
    def analyze_emotion(self, user_input):
        emotions = {
            "joy": 0.0,
            "sadness": 0.0,
            "anger": 0.0,
            "surprise": 0.0,
            "fear": 0.0
        }
        doc = self.nlp(user_input)
        emotions = {token.text.lower(): emotions.get(token.text.lower(), 0) + 1 for token in doc if token.text.lower() in emotions}
        
        return emotions
    
    def respond(self, user_input):
        emotions = self.analyze_emotion(user_input)
        max_emotion = max(emotions, key=emotions.get)
        response = f"The predominant emotion detected is {max_emotion}."
        self.text_to_speech(response)
        return response
    
    def recognize_speech(self, audio_source=None, language="en-US"):
        try:
            with sr.AudioFile(audio_source) as source:
                audio_data = self.speech_recognizer.record(source)
                text = self.speech_recognizer.recognize_google(audio_data, language=language)
                return text
        except Exception as e:
            self.logger.error(f"Error in recognize_speech function: {e}")
            return "Error: Speech recognition could not understand the audio or access the file."
    
    def perform_sentiment_analysis(self, text):
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        return sentiment_score
        
    def bert_nlu_processing(self, text):
        try:
            nlu_pipeline = pipeline("sentiment-analysis")
            result = nlu_pipeline(text)
            return result
        except Exception as e:
            self.logger.error(f"Error in bert_nlu_processing function: {e}")
            raise InvalidTextError("BERT NLU processing failed.")

def main():
    ai = AutomatedRealPersonSimulation()
    
    # Example usage of text_to_speech
    text = "Hello, how are you joy?"
    print(f"Input text: {text}")
    ai.text_to_speech(text)
    
    # Example usage of respond function
    response = ai.respond(text)
    print(f"Response: {response}")
    
    # Example usage of sentiment analysis
    sentiment_score = ai.perform_sentiment_analysis(text)
    print(f"Sentiment score: {sentiment_score}")
    
    # Example usage of BERT NLU processing
    nlu_result = ai.bert_nlu_processing(text)
    print(f"BERT NLU result: {nlu_result}")

if __name__ == "__main__":
    main()
