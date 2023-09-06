import cv2
import os
import imutils

personName='Abel'
dataPath='C:/Users/abel_/Desktop/Python/Reconocimeinto Facial/Data'

personPath=dataPath+'/'+personName

if not os.path.exists(personPath):
    print('Carpeta Creada: ',personPath)
    os.makedirs(personPath)

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

faceClassif=cv2.CascadeClassifier(cv2.data)

while True:
    ret, frame= cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(2)==27:
        break
    
cap.release()
cv2.destroyAllWindows()