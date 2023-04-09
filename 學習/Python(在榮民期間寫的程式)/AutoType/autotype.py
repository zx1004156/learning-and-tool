import pyautogui,keyboard
print('q是開始必殺技\n空白鍵是關掉程式')
while(1):
    if(keyboard.is_pressed('q')):
        pyautogui.typewrite(['up','up','down','down','left','right','left','right','b','a'],interval=0.3)
    elif keyboard.is_pressed('space'):
        break
