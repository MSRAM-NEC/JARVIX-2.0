# main.py

# Import our custom core modules
from core.speaker import say  # <-- Import the 'say' function directly
from core.listener import Listener
# from core.command_parser import CommandParser 

import time

if __name__ == "__main__":
    # The listener is still a class because it manages the microphone state
    listener = Listener()
    
    # Use the 'say' function for all speech
    say("Core systems initialized. JARVIX 2.0 is online and ready.")

    while True:
        command = listener.listen()

        if command:
            if "exit" in command or "goodbye" in command or "stop" in command:
                say("Deactivating. Goodbye!")
                break
            
            response = f"I have successfully received the command: {command}"
            say(response)
        else:
            # The listener already prints errors, so we can just provide a simple audio cue
            say("I didn't quite catch that.")

        time.sleep(1)