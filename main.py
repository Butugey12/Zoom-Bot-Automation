import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime


def sign_in(meetingid, pswd):
    # subprocess.call('C:\\myprogram.exe')
    subprocess.call(
        ["C:\\Users\\butug\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"])
    time.sleep(5)
    btn1 = pyautogui.locateCenterOnScreen('joinBtn1.png')
    pyautogui.moveTo(btn1)
    pyautogui.click()

    # meeting id button
    meetingIdButton = pyautogui.locateCenterOnScreen("meetingIdBtn.png")
    pyautogui.moveTo(meetingIdButton)
    pyautogui.click()
    pyautogui.write(meetingid)

    mediaBtn = pyautogui.locateAllOnScreen("mediaBtn.png")
    for i in mediaBtn:
        pyautogui.moveTo(i)
        pyautogui.click()
        time.sleep(3)
    joinBtn2 = pyautogui.locateCenterOnScreen("joinBtn2.png")
    pyautogui.moveTo(joinBtn2)
    pyautogui.click()


sign_in("8033493705", "QSC01N")
