
class firebase_handclap(object):
    def __init__(self, config,email="zunchero@gmail.com", pwd="123456"):
        import pyrebase
        self.firebase = pyrebase.initialize_app(config)
        auth = self.firebase.auth()
        self.user = auth.sign_in_with_email_and_password(email, pwd)
        self.db = self.firebase.database()

    def update(self, master, key, val):
        try:
            self.db.child(master).update({key:val})
        except:
            return False
    def getAll(self):
        return self.db.child("light").get().val()
    def get(self, master, child):
        return self.db.child(master).child(child).get().val()


if __name__ == "__main__":

    print("main")
    config = {
        "apiKey": "AIzaSyBXsQCOqIyYPGz-3ZwCezJwWsVfMkEOLqI",
        "authDomain": "handclap-2100f.firebaseapp.com",
        "databaseURL": "https://handclap-2100f.firebaseio.com",
        "storageBucket": "handclap-2100f.appspot.com"
    }

    mydb = firebase_handclap(config,"zunchero@gmail.com","123456")
    mydb.update("light","LED1",0)
    print(mydb.getAll())