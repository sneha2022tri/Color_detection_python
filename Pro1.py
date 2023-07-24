import cv2
import numpy as np 
cap=cv2.VideoCapture(0)  #It takes arguement if we type normal 0 without string or quotes then t will ask webcam access and if we type path of any video so it will run the project in video path#
while True:
    _,frame=cap.read() #Till the webcam is on , read the frames of video and keep creating its hsv frames#
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #There are two types of colors BGR:Blue gree Red and HSV:Hue saturation and value, we are converitng all the frames we getting into hsv frame.The advantage of hsv frame is that ,hsv frame are closest to humans , i.e humans can see the hsv frame from the closest#
    #detecting red color#
    low_red=np.array([161,155,84])#these values are the hsv values of low resolution red color#
    hight_red=np.array([179,255,255])#these are the hsv values of high resolution red#
    red_mask=cv2.inRange(hsv_frame,low_red,high_red)#the purpose of making this red_mask is that it will read only that color and wont read any color until and unless it founds red color//inRange method checks if first argument is between the second argumenet or not, if it is then it assigns the value to the given variable#
    red=cv2.bitwise_and(frame,frame,mask=red_mask)#bitwise operator will take two frames and do and operation btwn them#

    #detecting blue color#
    low_blue=np.array([94,80,2])
    high_blue=np.array([126,255,255])
    blue_mask=cv2.inRange(hsv_frame,low_blue,high_blue)
    blue=cv2.bitwise_and(frame,frame,mask=blue_mask)

    #detecting green color#
    low_green=np.array([25,52,72])
    high_green=np.array([102,255,255])
    green_mask=cv2.inRange(hsv_frame,low_green,high_green)
    green=cv2.bitwise_and(frame,frame,mask=green_mask)

    cv2.imshow("Frame",frame)
    cv2.imshow("Red",red)
    cv2.imshow("Blue",blue)
    cv2.imshow("Green",green)
    key=cv2.waitkey(1)
    if(key==27):
        break
