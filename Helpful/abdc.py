import pyautogui
import keyboard

while keyboard.is_pressed('a') == False:
 print(pyautogui.displayMousePosition())