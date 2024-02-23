import cv2
import face_recognition
from io import BytesIO
from PIL import Image 
import Model.database as db
from Model.user import User
import numpy as np


def authenticationUser(user):
     #Se obtiene el tiempo inicial
     tmI=cv2.getTickCount()
     
     imgUser = BytesIO(user.get_photo())
     image_array=np.asarray(bytearray(imgUser.read()),dtype=np.uint8)
     image = cv2.imdecode(image_array,cv2.IMREAD_COLOR)
     
     face_loc = face_recognition.face_locations(image)[0]
     face_image_encodings = face_recognition.face_encodings(image, known_face_locations=[face_loc])[0]

     cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

     while True:
          ret, frame = cap.read()
          if ret == False: break
          frame = cv2.flip(frame, 1)
          face_locations = face_recognition.face_locations(frame)
          if face_locations != []:
               for face_location in face_locations:
                    face_frame_encodings = face_recognition.face_encodings(frame, known_face_locations=[face_location])[0]
                    result = face_recognition.compare_faces([face_image_encodings], face_frame_encodings)
                    if result[0] == True:
                         text = user.get_username()
                         color = (125, 220, 0)
                         flag = True
                    else:
                         text = "Desconocido"
                         color = (50, 50, 255)
                         flag = False
                    cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2] + 30), color, -1)
                    cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), color, 2)
                    cv2.putText(frame, text, (face_location[3], face_location[2] + 20), 2, 0.7, (255, 255, 255), 1)
                   
               if timer(tmI,20):
                    cv2.destroyAllWindows()
                    return flag
               
          cv2.imshow("Frame", frame)
          key = cv2.waitKey(1)
          if key == 27:
               cv2.destroyAllWindows()
          
     cap.release()
     
     
'''
def convertToBinaryData(filename):
    try:
        with open(filename,'rb') as file:
            binaryData=file.read()
            return binaryData
    except:
        return 0 
'''
def timer(tmI,duration):
     tmT=(cv2.getTickCount()-tmI)/cv2.getTickFrequency()
     if tmT>=duration:
          return True
     
def frameToBinaryData(frame,format=".jpg"):
     _,encoded_frame=cv2.imencode(format,frame)
     return np.array(encoded_frame).tobytes()
     
     
def getPhotoUser():
     cap=cv2.VideoCapture(1)
     while True:
          cap.set(cv2.CAP_PROP_FRAME_WIDTH,2560)
          cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1440)
          ret,frame=cap.read()
          if ret == False: break
          frame = cv2.flip(frame, 1)
          face_locations = face_recognition.face_locations(frame)
          if face_locations != []:
               for face_location in face_locations:
                    text="Rostro"
                    color = (125, 220, 0)
                    cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2] + 30), color, -1)
                    cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), color, 2)
                    cv2.putText(frame, text, (face_location[3], face_location[2] + 20), 2, 0.7, (255, 255, 255), 1)
               
               return(frameToBinaryData(frame))
     cap.release()
     cv2.destroyAllWindows()

def searchUser(username,password):
    _userCurrent=db.verificationUser(username,password)
    if(_userCurrent):
        return _userCurrent
    else:
        return False

def createUser(username,password):
     db.createUser(username,password,getPhotoUser())
