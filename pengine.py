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
delayTime = .8
holdTime = 1.4
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
		if(pyautogui.pixelMatchesColor(1173, 337, (2, 128, 205))):
			lastTime = 0
	if(time.time() - 20> lastTime):
		print("end of round, initiated reset")
		pyautogui.click(x=1257, y=216) 
		time.sleep(0.05)
		pyautogui.click(x=1257, y=216) 
		while(False == pyautogui.pixelMatchesColor(1368, 738, (120, 149, 187))):
			time.sleep(0.1)
		time.sleep(0.5)
		pyautogui.click(x=1500, y=315) 
		time.sleep(0.01)
		pyautogui.click(x=1500, y=315) 
		while(False == pyautogui.pixelMatchesColor(677, 570, (2, 128, 205))):
			time.sleep(0.1)
		time.sleep(0.5)
		pyautogui.click(x=860, y=512) 
		time.sleep(0.01)
		pyautogui.click(x=860, y=512) 
		while(False == pyautogui.pixelMatchesColor(764, 996, (87, 30, 0))):
			time.sleep(0.1)
		time.sleep(0.5)
		pyautogui.click(x=1439, y=847) 
		time.sleep(0.01)
		pyautogui.click(x=1439, y=847)
		lastTime = time.time()
	arrowLowcation = pyautogui.locateOnScreen("yellow.png", region= (450,500,1000,1))
	if arrowLowcation is not None:
		lock = True
		crashed = True
		print(time.time() -lastTime)
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


		
			
			
 