import cv2
import numpy as np
import pyscreenshot as ImageGrab
import time
from keras.models import load_model
import pyautogui
import os
from keras.preprocessing import image
#processing the image
def process_image(image):
	original_image=image
	processed_image =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	return processed_image

def screen_record():
	
	#load image from model
	model=load_model('dino-model.h5')
	#5 seconds timer
	for i in list(range(4))[::-1]:
		print(i+1)
	time.sleep(1)
	last_time=time.time()
	while(True):    
		
            #grab the region of the screen
            # 1. open your google chrome
            # 2. type "chrome://dino" in your address bar
            # 3. now select "windows key+left arrow" or similar key
            #    according to your os to align to extreme left of
            #    your window
            # 4. make sure that the little screen that popped up
            #    should be away from chrome browser
		
		image1 = pyautogui.screenshot(region =(90,245,315,250))
		image1 = cv2.cvtColor(np.array(image1), cv2.COLOR_RGB2BGR)
	
		print('took {}'.format(time.time()-last_time))
		last_time=time.time()
		
		test_image = cv2.resize(image1,(50,50))

		pred = model.predict(test_image.reshape(1,50,50,3))
		print(pred)
		if(pred>0):
			#jump
			pyautogui.press('space')
			
		cv2.imshow('window',test_image)
		#press 'q' to exit the screen or press 'control+c'
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

screen_record()	 

