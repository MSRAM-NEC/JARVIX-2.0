# core/listener.py

import speech_recognition as sr

class Listener:
    def __init__(self):
        """Initializes the speech recognizer."""
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        # Adjust for ambient noise once at the start
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

    def listen(self):
        """
        Captures audio from the microphone and converts it to text.
        Returns the recognized text as a lowercase string, or None if failed.
        """
        with self.microphone as source:
            print("\nListening...")
            self.recognizer.pause_threshold = 1
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            # Using Google's free web API for recognition
            query = self.recognizer.recognize_google(audio, language='en-us')
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            # This error means the recognizer couldn't understand the audio
            return None
        except sr.RequestError as e:
            print(f"Recognition service error; check internet. Error: {e}")
            return None
        except Exception as e:
            print(f"An unknown error occurred during listening: {e}")
            return None