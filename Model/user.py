class User:
    def __init__(self,id_user,username,password,photo):
        self._id_user=id_user
        self._username=username
        self._password=password
        self._photo=photo
        
    def get_username(self):
        return self._username
    def set_username(self,newuser):
        self._username=newuser
        
    def get_password(self):
        return self._password
    
    def set_password(self,newpassword):
        self._password=newpassword
        
    def get_photo(self):
        return self._photo
    
    def set_photo(self, newphoto):
        self._photo=newphoto
