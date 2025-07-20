import time
import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        print(f"Current position is x, y: {x}, {y}")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopped")