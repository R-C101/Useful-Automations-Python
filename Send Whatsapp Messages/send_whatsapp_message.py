import pyautogui as pag

x,y= pag.locateCenterOnScreen('/Users/rishit/Desktop/Screenshot 2022-11-03 at 6.24.10 PM.png')
x=x/2 #for macbooks retina screen
y=y/2 #remove if not mac
pag.click( (x,y) , duration = 1)
pag.write('Hello Anish', 0.2)
pag.press('enter')