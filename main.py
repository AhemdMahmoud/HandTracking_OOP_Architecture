import cv2
from HandTrackingModule import HandTrackingModule
import time



pfTime=0
ctTime=0
cap = cv2.VideoCapture(0)
obj=HandTrackingModule()
while True:
    _,img=cap.read()
    img=obj.findHands(img)
    ctTime=time.time()
    fps=1/(ctTime-pfTime)
    pfTime=ctTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow('Image',img) # Display the image in a window named "Image"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break