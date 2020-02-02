import pyautogui
import time 
import threading

def doTrick():
	global lock
	while True:
		if lock:
			time.sleep(0.01)
		else:
			pyautogui.keyDown('up')

lock = True
t = threading.Thread(target = doTrick)
t.start()
i = 0
delayTime = .8
holdTime = 1.4
lastTime = time.time()
while True:
	if(time.time() -20 > lastTime):
		pyautogui.click(x=984, y=832) 
		time.sleep(1)
		pyautogui.click(x=1175, y=383) 
		time.sleep(0.01)
		pyautogui.click(x=1175, y=383) 
		time.sleep(3)
		pyautogui.click(x=1493, y=443) 
		time.sleep(0.01)
		pyautogui.click(x=1493, y=443) 
		time.sleep(4)
		pyautogui.click(x=831, y=550) 
		time.sleep(3)
		pyautogui.click(x=1439, y=847) 
		time.sleep(0.01)
		pyautogui.click(x=1439, y=847) 
		time.sleep(3)
		lastTime = time.time()
	arrowLowcation = pyautogui.locateOnScreen("yellow.png", region= (450,500,1000,1))
	if arrowLowcation is not None:
		lock = True
		lastTime = time.time()
		print("saw somthing")
		if arrowLowcation[0] < 960:
			print("left")
			time.sleep(delayTime)
			start = time.time()
			while time.time() - holdTime < start:
				pyautogui.keyDown('right')
			pyautogui.keyUp('right')
		else:
			print("right")
			time.sleep(delayTime)
			start = time.time()
			while time.time() - holdTime < start:
				pyautogui.keyDown('left')
			pyautogui.keyUp('left')
		lock = False


		
			
			
 