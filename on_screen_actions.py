# The script's aim is to perform and actino in screen considering an x, y coordinate is given
import pyautogui

# coordinates
# x, y = 1201, 893

# duration is set for smooth movement
# pyautogui.moveTo(x, y, duration=0.5)
# pyautogui.click()

# x, y = 749, 582
# pyautogui.moveTo(x, y, duration=0.5)
# pyautogui.click()
# pyautogui.write("Thank you that works!", interval=0.05)
# pyautogui.press('enter')

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    print("Screenshot saved as screenshot.png")

def click_a_spot(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()
