import cv2
import mediapipe as mp
import time
import paho.mqtt.publish as publish
 
#raspberry pi ip address
MQTT_SERVER = "192.168.0.104" 
MQTT_PATH = "test_channel"

mp_draw=mp.solutions.drawing_utils
mp_hand=mp.solutions.hands

tipIds=[4,8,12,16,20]

cap=cv2.VideoCapture(1)

with mp_hand.Hands(min_detection_confidence=0.5,
               min_tracking_confidence=0.5) as hands:
    while True:
        ret,image=cap.read()
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable=False
        results=hands.process(image)
        image.flags.writeable=True
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList=[]
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands=results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h,w,c=image.shape
                    cx,cy= int(lm.x*w), int(lm.y*h)
                    lmList.append([id,cx,cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
        fingers=[]
        if len(lmList)!=0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            finger_counter = fingers.count(1)
            
            #print(finger_counter)
            publish.single(MQTT_PATH, finger_counter, hostname=MQTT_SERVER)
            if finger_counter == 5:
                cv2.putText(image, 'Forward', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)

            elif finger_counter == 4:
                cv2.putText(image, 'Backward', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)

            elif finger_counter == 0:
                cv2.putText(image, 'Stop', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)

            elif finger_counter == 2:
                cv2.putText(image, 'Right', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)

            elif finger_counter == 1:
                cv2.putText(image, 'Left', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)


        cv2.imshow("result",image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

cap.release()
cv2.cv2.destroyAllWindows()


 