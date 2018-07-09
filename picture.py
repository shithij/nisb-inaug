import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.moveTo(270,1050,duration=2)
pyautogui.click(270,1050)
pyautogui.typewrite("Paint",0.5)
pyautogui.typewrite(['enter'])

pyautogui.click(389,81)
pyautogui.moveTo(8,532)
pyautogui.dragTo(383,238,duration=3)
pyautogui.dragTo(808,529,duration=3)
pyautogui.moveTo(708,460,duration=1)
pyautogui.dragTo(1190,216,duration=3)
pyautogui.dragTo(1630,458,duration=3)
pyautogui.click(491,76)
pyautogui.moveTo(639,246,duration=1)
pyautogui.dragTo(789,394,duration=3)
pyautogui.click(389,81)
pyautogui.moveTo(639,730,duration=1)
pyautogui.dragTo(737,595,duration=3)
pyautogui.dragTo(849,730,duration=3)
pyautogui.moveTo(737,595,duration=1)
pyautogui.dragTo(1026,538,duration=3)
pyautogui.moveTo(849,730,duration=1)
pyautogui.dragTo(1138,673,duration=3)
pyautogui.dragTo(1026,538,duration=3)
d=150
pyautogui.moveTo(836,715,duration=1)
pyautogui.dragRel(0,d,duration=3)
pyautogui.moveTo(649,715,duration=1)
pyautogui.dragRel(0,d,duration=3)
pyautogui.dragRel(187,0,duration=3)
pyautogui.dragTo(1125,808,duration=3)
pyautogui.dragTo(1125,676,duration=3)
l=75
b=187/3
pyautogui.moveTo(649+b,865,duration=1)
pyautogui.dragRel(0,-l,duration=3)
pyautogui.dragRel(b,0,duration=3)
pyautogui.dragRel(0,l,duration=3)

pyautogui.click(731,94)
time.sleep(1)
pyautogui.click(791,322)
pyautogui.click(764,832)
pyautogui.moveTo(0,0,duration=1)
