#! /usr/bin/python3
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

config = {
        "apiKey": "AIzaSyBXsQCOqIyYPGz-3ZwCezJwWsVfMkEOLqI",
        "authDomain": "handclap-2100f.firebaseapp.com",
        "databaseURL": "https://handclap-2100f.firebaseio.com",
        "storageBucket": "handclap-2100f.appspot.com"
    }
mydb = firebase_handclap(config,"zunchero@gmail.com","123456")


import speech_recognition as sr

r=sr.Recognizer()
number=0
print(sr.Microphone.list_microphone_names())
mic = sr.Microphone()
for i, mic_name in enumerate(sr.Microphone.list_microphone_names()):
    if("samson" in mic_name):
        mic = sr.Microphone(device_index=i)
        number=i
        print("samson")
        break

flag = True
with mic as source:


    while True:
        r.energy_threshold = 2300
        r.dynamic_energy_threshold = False
        print("SAY SOMETHING")

        try:
            audio = r.listen(source, timeout=1.5)
            print("end record")
            speech = str(r.recognize_google(audio, language="th"))
            print("TEXT :" + speech)
        except:
            continue
        if (speech.lower() == "ok google") or speech.lower() == "hey google":
            falg = True
            continue

        if flag == True:
            if  "เปิดไฟ" in speech:
                mydb.update("light", "LED1", 1)
                print("เปิดแล้วจ้า")
            elif "ปิดไฟ" in speech:
                mydb.update("light", "LED1", 0)
                print("ปิดแล้วจ้า")

