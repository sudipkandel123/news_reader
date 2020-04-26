import speech_recognition as sr  

# get audio from the microphone                                                                       
r = sr.Recognizer()     
                                                                              
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   
    
voice = r.recognize_google(audio)

try:
    print("You said " + r.recognize_google(audio))
    if voice == 'news':
        print("okay ")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))