import mysql.connector
from PIL import Image
import io
from Model.user import User

conexion=mysql.connector.connect(
    host="db4free.net",
    user="chrisbel2000",
    password="3rd@gJk7#NgV2Ha",
    database="argprom42023"
)
def getPhoto(iduser):
    cursor = conexion.cursor()
    query='SELECT photo FROM USER WHERE idUSER = %s'
    cursor.execute(query,(iduser,))
    result=cursor.fetchone()
    if result:
        photo_bytes=result[0]
        img = Image.open(io.BytesIO(photo_bytes))
        img.show()
    
    cursor.close()

def createUser(username,password,photo):
    cursor = conexion.cursor()
    query = 'INSERT INTO USER (idUSER, username, password, photo) VALUES (%s, %s, %s, %s)'
    newUser = ((countUsers()+1), username, password,photo)
    cursor.execute(query, newUser)
    conexion.commit()
    cursor.close()
    
def verificationUser(username,password):
    cursor = conexion.cursor()
    query = 'SELECT * FROM USER WHERE username = %s AND password = %s'
    cursor.execute(query, (username,password))
    result=cursor.fetchone()
    cursor.close()
    if result:
        _userCurrent=User(result[0],result[1],result[2],result[3])
        return _userCurrent
    else:
        return False

def countUsers():
    cursor=conexion.cursor()
    query='SELECT COUNT(*) as total FROM USER'
    cursor.execute(query)
    result=cursor.fetchone()
    cursor.close()
    return result[0]
