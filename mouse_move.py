import pyautogui
import time
class mouse :
    def mouse_move():
        time.sleep(2)
        pyautogui.moveTo(250,65)
        pyautogui.click()
        #pyautogui.hotkey('ctrl','v')
        #pyautogui.press('enter')
        time.sleep(3)
        pyautogui.moveTo(530,800)
        pyautogui.click()

mouse.mouse_move()