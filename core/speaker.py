# core/speaker.py

import pyttsx3

def say(text):
    """
    Speaks the given text using the 'sapi5' driver.
    This version is designed to be highly reliable on Windows and includes error handling.
    """
    # Do nothing if the text is empty
    if not text:
        return

    engine = None  # Ensure the 'engine' variable exists outside the try block
    try:
        # STEP 1: Initialize the engine, explicitly specifying the 'sapi5' driver.
        # This is the most important fix for Windows systems.
        engine = pyttsx3.init('sapi5')
        
        # STEP 2: A crucial check to ensure the engine object was created successfully.
        if not engine:
            raise RuntimeError("The pyttsx3 engine could not be initialized. Your system may be missing a TTS driver.")

        # STEP 3: Set properties on the now-guaranteed valid engine object.
        engine.setProperty('rate', 180)  # Speed of the voice
        engine.setProperty('volume', 1.0) # Volume level (0.0 to 1.0)
        
        # STEP 4: Print to console and speak the text.
        print(f"JARVIX: {text}")
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        # If any part of the process fails, print a clear error message.
        print(f"FATAL: An error occurred in the speaker module. Cannot produce speech. Error: {e}")
    
    finally:
        # STEP 5: Cleanly shut down the engine instance after speaking.
        # This is good practice to release resources.
        if engine is not None:
            engine.stop()