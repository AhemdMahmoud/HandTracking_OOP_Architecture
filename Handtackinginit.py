import  cv2
import mediapipe as mp
import time
mpHands=mp.solutions.hands
hands=mpHands.Hands()

mp_drawing = mp.solutions.drawing_utils

pfTime=0
ctTime=0

cap = cv2.VideoCapture(0)

while True:

    _,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    # cv2.imshow('Image',imgRGB) # Display the image in a window named "Image" 
    # print(results.multi_hand_landmarks)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                # print(id,lm)
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)   
                # print(id,cx,cy)
                if id==8:
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

            mp_drawing.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
     # Display the image in a window named "Image"


    ctTime=time.time()
    fps=1/(ctTime-pfTime)
    pfTime=ctTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow('Image',img) # Display the image in a window named "Image"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
