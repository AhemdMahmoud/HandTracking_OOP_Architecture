import  cv2
import mediapipe as mp
import time


# pfTime=0
# ctTime=0

# cap = cv2.VideoCapture(0)
class HandTrackingModule: 
    def __init__(self,static_image_mode=False,max_num_hands=2,min_detection_confidence=0.5,min_tracking_confidence=0.5):
        self.static_image_mode=static_image_mode
        self.max_num_hands=max_num_hands
        self.min_detection_confidence=min_detection_confidence
        self.min_tracking_confidence=min_tracking_confidence
        self.mpHands=mp.solutions.hands
        self.hands =self.mpHands.Hands()
        self.mp_drawing = mp.solutions.drawing_utils

        
    def findHands(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_drawing.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self,img,handNo=0,draw=True):
        lmList=[]
        if self.results.multi_hand_landmarks:
            self.results.multi_hand_landmarks[handNo]
            for handLms in self.results.multi_hand_landmarks:
                for id,lm in enumerate(handLms.landmark):
                    h,w,c=img.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)   
                    lmList.append([id,cx,cy])
                if draw:
                    self.mp_drawing.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return lmList




def main():
    pfTime=0
    ctTime=0
    cap = cv2.VideoCapture(0)
    obj=HandTrackingModule()
    while True:
        _,img=cap.read()
        img=obj.findHands(img)
        limlsit=obj.findPosition(img,draw=False)
        if len(limlsit)!=0:
            print(limlsit[4])
        ctTime=time.time()
        fps=1/(ctTime-pfTime)
        pfTime=ctTime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        cv2.imshow('Image',img) # Display the image in a window named "Image"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()