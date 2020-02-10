import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        print("SAY SOMETHING");
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
        print("TIME OVER")
        try:
            print("TEXT :" + r.recognize_google(audio, language = 'th'));
        except:
            pass;

        speech = str(r.recognize_google(audio, language = 'th',show_all=True))
        
        if  "เปิดไฟ" in speech:
            print("เปิดแล้วจ้า")
        elif "ปิดไฟ" in speech:
            print("ปิดแล้วจ้า")
        else:
            pass;
        continue