import pyautogui 
import pygetwindow as gw
from PIL import ImageOps
import subprocess
import time

time.sleep(1)

apple_script = '''
tell application "Google Chrome"
    activate
    make new window
    tell window 1
        set URL of active tab to "https://elgoog.im/dinosaur-game/"
    end tell
end tell
'''

subprocess.run(["osascript", "-e", apple_script])
time.sleep(2)

pyautogui.press('space')
time.sleep(2)

while True:
    active_window = gw.getActiveWindow()
    if 'Google Chrome' in active_window:
        img = pyautogui.screenshot(region=(310,600,100,80))
        # Convert to grayscale and get pixel data
        gray_img = ImageOps.grayscale(img)
        pixels = gray_img.getdata()

        # Check if there's a non-white pixel (indicating an obstacle)
        if any(pixel < 100 for pixel in pixels):  # threshold can be adjusted
            print("Obstacle detected! Jumping.")
            pyautogui.press('space')  # or 'up'
        else:                                   
            print("No obstacle.")   

    else:
        print('Chrome not active')
        break

                                                                

