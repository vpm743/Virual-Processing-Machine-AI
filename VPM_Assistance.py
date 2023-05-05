import pyttsx3
import random
import os
import pyjokes
import webbrowser
import wikipedia
import datetime
import speech_recognition as spre
vpm_voice_engine=pyttsx3.init("sapi5")
vpm_voices=vpm_voice_engine.getProperty("voices")
vpm_voice_engine.setProperty("voices",vpm_voices[0].id)

def speak(audio):
    vpm_voice_engine.say(audio)
    vpm_voice_engine.runAndWait()
def wish():
    wishtime=(datetime.datetime.now().hour)
    if wishtime>0 and wishtime<12:
        speak("Good Morning Sir")
    elif wishtime>=12 and wishtime<16:
        speak("Good afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Virtual Partner Machine. V P M")
    speak("How can i help you ")
def command_input():
    rechno=spre.Recognizer()
    with spre.Microphone() as source:
        print("Listening.......")
        pause_threshold=1
        audio_input=rechno.listen(source)

    try:
        print("RECOIGNIZING.....")
        user_query=rechno.recognize_google(audio_input,language="en-in")
        print(f"Master's Command {user_query}\n")
        speak(user_query)
    except Exception as ex:
        
        print("Can't Get It Master. Say It Again Please")
        speak("Can't Get It Master. Say It Again Please")
        return "None"
    return user_query
if __name__=="__main__":
    wish()
    while True:
        input_query=command_input().lower()
        if "wikipedia" in input_query:
            print("Searching ......")
            speak("Searching ......")
            input_query=input_query.replace("wikipedia","")
            query_result=wikipedia.summary(input_query,sentences=2)
            speak("According To Wikipedia")
            print(query_result)
            speak(query_result)
        elif "open google" in input_query:
            speak("Opening Google Master")
            webbrowser.open_new("https://www.google.com")

        elif "play online song" in input_query:
            speak("Playing Song Master")
            webbrowser.open_new("https://www.youtube.com/watch?v=vdY5SFZBgnk&list=PLO7-VO1D0_6M1xUjj8HxTxskouWx48SNw")
        elif "open whatsapp" in input_query:
            speak("opening whatsapp Master")
            webbrowser.open_new("https://web.whatsapp.com/")
        elif "play offline song" in input_query:
            music_paly_dir="D:\Songs\All"
            songs_list=os.listdir(music_paly_dir)
            song_list_length=len(songs_list)
            #print(songs_list)
            os.startfile(os.path.join(music_paly_dir,songs_list[random.randint(0,song_list_length-1)]))
        elif "the time" in input_query:
            time_say=datetime.datetime.now().strftime("%H:%M:%S")
            print(time_say)
            speak(f"sir, the time is {time_say}")
        elif "open chrome" in input_query:
            chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chrome_path)
        elif "tell me a joke" in input_query:
            My_joke = pyjokes.get_joke(language="en", category="all")
            print(My_joke)
            speak(My_joke)
        elif "quit" in input_query:
            print("Good Day Master")
            speak("Good Day Master")
            break
