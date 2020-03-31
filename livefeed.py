import requests
import numpy as np 
import cv2 
import os
i=0
def hand_wash(sample):
	if(sample.shape[0]==-1):
		sample=cv2.imread("test111.jpg")
	#roi=img[:,:]
	sample=sample[200:,150:]
	min_HSV = np.array([0, 58, 30], dtype = "uint8")
	max_HSV = np.array([33, 255, 255], dtype = "uint8")
	imageHSV = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV)
	skinRegionHSV = cv2.inRange(imageHSV, min_HSV, max_HSV)
	contours,_=cv2.findContours(skinRegionHSV,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	areas = [cv2.contourArea(c) for c in contours]
	#lol=cv2.erode(skinRegionHSV, (5,5))
	max_index=0
	max_index = np.argmax(areas)
	cnt=contours[max_index]
	x,y,w,h = cv2.boundingRect(cnt)
	cv2.rectangle(sample,(x,y),(x+w,y+h),(0,255,0),3)
	skinHSV = cv2.bitwise_and(sample, sample, mask = skinRegionHSV)


#	cv2.rectangle(sample,(274,150), (615,500),(0,255,0))
	
	#cv2.rectang
	#fgMask = backSub.apply(bgd)
	cv2.imshow('Frame', skinRegionHSV)

    #cv2.imshow('FG Mask', fgMask)
	return sample


while True:
	url="http://192.168.1.19:8080/shot.jpg"
	img_data=requests.get(url)
	img_arr=np.array(bytearray(img_data.content),dtype=np.uint8)
	img=cv2.imdecode(img_arr,-1)
	img=hand_wash(img)
	cv2.imshow('livefeed',img)
	#os.system("mpg123 welcome.mp3") 
	cv2.imwrite('test.jpg', img)
	#i=i+1

	if (cv2.waitKey(1)) == ord('q'):
	 cv2.destroyAllWindows()
	 break