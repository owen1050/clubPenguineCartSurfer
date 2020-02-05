import pyautogui
import time 
import threading

def doTrick():
	global lock
	while True:
		time.sleep(0.01)
		if lock:
			pass
		else:
			pyautogui.keyDown('up')

lock = True
t = threading.Thread(target = doTrick)
t.start()
i = 0
counter = 0
delayTime = .8
holdTime = 1.1
lastTime = time.time()
crashed = True
while True:
	if(time.time() - 10> lastTime and crashed):
		pyautogui.keyDown('space')
		time.sleep(0.05)
		pyautogui.keyDown('space')
		time.sleep(0.5)
		crashed = False
		print("presssed space to try and recover")
		if(pyautogui.pixelMatchesColor(1173, 450, (2, 128, 205))):
			lastTime = 0
	if(time.time() - 20> lastTime):
		counter = counter + 1
		print("end of round, initiated reset")
		pyautogui.click(x=1200, y=370) 
		time.sleep(0.05)
		pyautogui.click(x=1200, y=370) 
		while(False == pyautogui.pixelMatchesColor(1271, 848, (120, 149, 187))):
			time.sleep(0.1)
		time.sleep(0.5)
		pyautogui.click(x=1400, y=450) 
		time.sleep(0.01)
		pyautogui.click(x=1400, y=450) 
		while(False == pyautogui.pixelMatchesColor(750, 525, (2, 128, 205))):
			time.sleep(0.1)
		time.sleep(0.5)
		pyautogui.click(x=860, y=622) 
		time.sleep(0.01)
		pyautogui.click(x=860, y=622) 
		while(False == pyautogui.pixelMatchesColor(809, 1021, (87, 30, 0))):
			time.sleep(0.1)
		time.sleep(0.5)
		pyautogui.click(x=1289, y=617) 
		time.sleep(0.01)
		pyautogui.click(x=1289, y=617)  
		lastTime = time.time()
		print("Begining round " + str(counter))
	arrowLowcation = pyautogui.locateOnScreen("yellow.png", region= (450,500,1000,1))
	if arrowLowcation is not None:  
		lock = True
		crashed = True
		lastTime = time.time()
		if arrowLowcation[0] < 960:
			print("saw somthing left, turning right")
			time.sleep(delayTime)
			start = time.time()
			while time.time() - holdTime < start:
				pyautogui.keyDown('right')
			pyautogui.keyUp('right')
		else:
			print("saw somthing right, turning left")
			time.sleep(delayTime)
			start = time.time()
			while time.time() - holdTime < start:
				pyautogui.keyDown('left')
			pyautogui.keyUp('left')
		lock = False
