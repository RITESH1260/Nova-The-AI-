import pyttsx3     
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit as kit
import subprocess
import platform

# set the engine to initiate commands
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# voice[0] for male speech and voice[1] for female speech 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
# started by wishing you message
def wishMe():
    # speak("welcome Ritesh and ") 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:  
        speak('Good Morning sir!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon sir!')
    else:
        speak('Good Evening sir!')
        
    speak('I am Nova. Please tell me how may i help you today?')
    
def takeCommand():
    #it takes microphone input from the user and returns string output#
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 0.6
        audio = r.listen(source)
        
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
        
    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query  

def check_bluetooth_status():
    """Check if Bluetooth is ON or OFF"""
    system = platform.system()
    
    if system == "Windows":
        result = subprocess.run(
            ['powershell', '-Command', 
             'Get-PnpDevice -Class Bluetooth | Select-Object Status'],
            capture_output=True, text=True
        )
        if "OK" in result.stdout:
            return True  # Bluetooth ON hai
        else:
            return False  # Bluetooth OFF hai
    
    elif system == "Linux":
        result = subprocess.run(
            ['bluetoothctl', 'show'],
            capture_output=True, text=True
        )
        if "Powered: yes" in result.stdout:
            return True
        else:
            return False

def toggle_bluetooth():
    """Bluetooth ON/OFF karo"""
    system = platform.system()
    status = check_bluetooth_status()
    
    if system == "Windows":
        if status:  # Agar ON hai → OFF karo
            subprocess.run([
                'powershell', '-Command',
                'Get-PnpDevice -FriendlyName "Bluetooth*" | Disable-PnpDevice -Confirm:$false'
            ])
            speak("Bluetooth band kar diya")
        else:  # Agar OFF hai → ON karo
            subprocess.run([
                'powershell', '-Command',
                'Get-PnpDevice -FriendlyName "Bluetooth*" | Enable-PnpDevice -Confirm:$false'
            ])
            speak("Bluetooth chalu kar diya")
    

#---------------------Main-body--------------------------
     
if __name__ == "__main__":
    wishMe()
    # if 1:
    while True:
        query = takeCommand().lower()
        
        #logic for executing tasks bases on query#
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2) 
            speak('According to Wikipedia')
            speak(results)
            print(results)
            
            speak("Can i do something for you sir")
            
        elif "hello Nova" in query or "hi nova" in query or "hi Innova" in query or "hay Nova" in query or " Innova" in query:
            speak("hello sir. Are you feel happy today")
            
        elif " han Nova " in query or "sahi keh rahe ho tum nova" in query:
            speak("so we make a interested according to your joy , sir...  ")
            
        elif "nova bura lag raha hai" in query or "aaj ka din acha nahi gya" in query:
            speak("koi nahi sabka din ek jesa nahi hota . sab thik ho jayega")
            
        elif "nova kya tum ho" in query:
            speak("haa sir, mai yahi hu aapke liye aap chinta na kare")            
            
            
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
           
            speak("youtube khol diya sir!...")
            speak("Can i do something for you sir")
            
            
            
        

        elif 'play on youtube' in query or 'youtube par chalao' in query:
            try:
                speak("Kya play karna hai sir?")
                song = takeCommand()

                if song:
                    speak(f"{song} play kar raha hoon sir")
                    kit.playonyt(song)
                    speak("Enjoy sir, aur kuch?")
                else:
                    speak("Sorry sir, samajh nahi aaya")

            except Exception as e:
                speak("Sorry sir, error aa gaya")
                print(e)
            
        # elif 'search on youtube' in query:
        #     try:
        #         speak("Kya search karna hai sir?")
        #         search_query = takeCommand()
        #         if search_query:
        #             search_query = search_query.replace(" ", "+")
        #             webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
        #             speak(f"youtube par search ker diya hai sir")
        #             speak("Can i do something for you sir")
        #         else:
        #             speak("sorry sir, kuch problem aa gayi")
                    
        #     except Exception as e:
        #         speak("sorry sir, kuch error aa gya hai ")
        #         print(e)
            
            
        elif 'close youtube' in query:
            os.system('taskkill /f /im chrome.exe')
            speak("youtube close ker diya hai sir")
            speak("Can i do something for you sir")
          
            
        elif 'open google' in query:
            webbrowser.open('google.com')
            speak("google khol diya sir")
            speak("Can i do something for you sir")
            
        elif 'search on google' in query:
            try:
                speak("Kya search karna hai sir?")
                search_query = takeCommand()
                if search_query:
                    search_query = search_query.replace(" ", "+")
                    webbrowser.open(f"https://www.google.com/results?search_query={search_query}")
                    speak(f"google par search ker diya hai sir")
                    speak("Can i do something for you sir")
                else:
                    speak("sorry sir, kuch problem aa gayi")
                    
            except Exception as e:
                speak("sorry sir, kuch error aa gya hai ")
                print(e)
            
        elif 'close google' in query:
            os.system('taskkill /f /im chrome.exe')
            speak("google close ker diya hai sir")
            speak("Can i do something for you sir")

            
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
            speak("stackoverflow khol diya sir")
            speak("Can i do something for you sir")
                     
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strTime}')
            print(f'Sir, the time is {strTime}')
            speak("Can i do something for you sir")
            
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
            speak("instagram open ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'search on instagram' in query:
            try:
                speak("Kya search karna hai sir?")
                search_query = takeCommand()
                if search_query:
                    search_query = search_query.replace(" ", "+")
                    webbrowser.open(f"https://www.instagram.com/results?search_query={search_query}")
                    speak(f"instagram par search ker diya hai sir")
                    speak("Can i do something for you sir")
                    try:
                        speak("search kya mai aapki or madad ker sakta hu")
                        search_query = takeCommand()
                        if search_query:
                            search_query = search_query.replace(" ","+")
                            webbrowser.open(f"https://www.instagram.com/results?search_query={search_query}")
                            speak(f"Mene aapke liye ek or baar search ker diya hai sir")
                            speak("Can i do something for you sir")
                        else:
                            speak("sir, kuch problem ho gayi")
                    except Exception as e:
                        speak("sorry sir, kuch error aa gya hai ")
                        print(e)       
                            
                else:
                    speak("sorry sir, kuch problem aa gayi")
                    
            except Exception as e:
                speak("sorry sir, kuch error aa gya hai ")
                print(e)   
        
        elif "open instagram profile" in query:
            speak("kis ka profile kholna hai sir?")
            username = takeCommand()
            webbrowser.open(f"https://www.instagram.com/{username}/")
            speak(f"{username} ka profile open kar diya hai sir")
            
        elif "open instagram reels" in query or "open reels" in query:
            webbrowser.open("https://www.instagram.com/reels/")
            speak(" instagram reels open ker diya hai sir...")
            
        elif "open instagram chats" in query or "instagram messages" in query or "messages" in query or "chats" in query:
            webbrowser.open("https://www.instagram.com/direct/inbox/")
            speak("instagram chats open ho gya hai sir...")
            
            
        elif 'close instagram' in query:
            os.system('taskkill /f /im Instagram.exe')
            speak("instagram close ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
            speak("facebook open ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'close facebook' in query:
            os.system('taskkill /f /im Facebook.exe')
            speak("facebook close ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'open twitter' in query:
            webbrowser.open('twitter.com')
            speak("twitter open ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'search on twitter' in query:
            try:
                speak("Kya search karna hai sir?")
                search_query = takeCommand()
                if search_query:
                    search_query = search_query.replace(" ", "+")
                    webbrowser.open(f"https://www.twitter.com/results?search_query={search_query}")
                    speak(f"Twitter par search ker diya hai sir")
                    speak("Can i do something for you sir")
                else:
                    speak("sorry sir, kuch problem aa gayi")
                    
            except Exception as e:
                speak("sorry sir, kuch error aa gya hai ")
                print(e)
            
        
            
        elif 'close twitter' in query:
            os.system('taskkill /f /im Twitter.exe')
            speak("twitter close ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'open github' in query:
            webbrowser.open('github.com')
            speak("github open ker diya hai sir")
            speak("Can i do something for you sir")
            
        
            
        elif 'close github' in query:
            os.system('taskkill /f /im GitHubDesktop.exe')
            speak("github close ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'open file explorer' in query:
            webbrowser.open('file explorer')
            os.startfile('C:\\Users\\Ritesh\\Desktop')
            speak("file explorer open ker diya hai sir")
            speak("Can i do something for you sir")
            
        # Warning: explorer.exe is also responsible for the Windows taskbar and desktop. Killing it may temporarily hide your taskbar. It will restart automatically in a few seconds.
            
        elif ' open VScode ' in query:
            code = "C:\\Users\\Ritesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code)
            speak("vs code open ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'close vs code' in query:
            os.system('taskkill /f /im Code.exe')
            speak("vs code close ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'open chrome ' in query:
            code = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(code)
            speak("chrome browser open ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'close chrome' in query:
            os.system('taskkill /f /im chrome.exe')
            speak("chrome browser close ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif ' open mysql' in query:
            code = "C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe"
            os.startfile(code)
            speak("mysql workbench open ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'close mysql' in query:
            os.system('taskkill /f /im MySQLWorkbench.exe')
            speak("mysql workbench close ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'open cmd' in query:
            os.system('start cmd')
            speak("command prompt open ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'close cmd' in query:
            os.system('taskkill /f /im cmd.exe')
            speak("command prompt close ker diya hai sir")
            speak("Can i do something for you sir")
            
            
        elif 'open excel' in query:
            code = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.system('start excel')
            speak("mene excel open ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif 'close excel' in query:
            os.system('taskkill /f /im EXCEL.exe')
            speak("Excel close ker diya hai sir")
            speak("Can i do something for you sir")
            
        elif " whatsapp" in query:
            speak("whatspp open ho raha hai sir...")
            webbrowser.open("https://web.whatsapp.com")
            
            
        elif "open whatsapp" in query or "open whatsapp web "in query:
            speak("whatsapp open ker raha hu sir ")
            # Path to Chrome (update if different on your system)
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s"

            # Register Chrome browser
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

            # Open WhatsApp Web
            webbrowser.get('chrome').open("https://web.whatsapp.com")

            speak("WhatsApp Web is now open")
            speak("Can I do something else for you sir")
            
        # elif "send whatsapp inbox" in query:
        #     speak("tell me the number with country code")
        #     number = input("Enter number (with +91...): ")
            
        #     speak("what message should i send sir?")
        #     message = takeCommand().lower()
            
        #     kit.sendwhatmsg_instantly(number, message, wait_time=15, tab_close=True)

        #     speak("Message sent successfully")
    
    
    
    
    
    
    
    
    
    
    
        
            # Your contact list
            contacts = {
            "ritesh": "+919717218269",
            "manish": "+919205356272",
            "raju bhaiya": "+918368536704",
            "sidharth" or "Siddharth cs" : "+917303923938"
            }

        elif "send message to" in query or "whatsapp message Tu" in query:

            # Extract name from voice query
            name = query.replace("send message to", "").replace("whatsapp message Tu", "").strip().lower()

            if name in contacts:
                number = contacts[name]

                speak(f"What message should I send to {name}?")
                message = takeCommand().lower()

                speak("Sending message, please wait")

                kit.sendwhatmsg_instantly(number, message, wait_time=15, tab_close=True)

                speak(f"Message sent to {name}")

            else:
                speak("Contact not found in your list")
        
        
        
        
        
        
        
        
            
        elif 'who are you' in query or 'kon ho tum' in query or "kaun ho tum" in query:
            speak("I am advance ai assistent name Nova. which is made by the Ritesh and who is gives commands and query to operate all actions.")
            
        
        
        elif "bluetooth" in query:
            status = check_bluetooth_status()
            
            if status:
                speak("Bluetooth is now on, Can you want to Off it?")
                confirmation = takeCommand().lower()
                if "haan" in confirmation or "yes" in confirmation or "band" in confirmation:
                    toggle_bluetooth()
                else:
                    speak("okk, Bluetooth ON rehne deta hoon")
            else:
                speak("Bluetooth is now Off, Can you want to On it?")
                confirmation = takeCommand().lower()
                if "haan" in confirmation or "yes" in confirmation or "chalu" in confirmation:
                    toggle_bluetooth()
                else:
                    speak("Theek hai, Bluetooth OFF rehne deta hoon")
                    
           
            
        
        elif "quit" in query or "bye bye " in query :
            speak("bye bye sir, let we work together after some time")
            break
        
        elif "shutdown" in query or "power off" in query:
            speak("Are you sure you want to shut down the system?")
            query = takeCommand().lower()

        elif "yes" in query or "confirm" in query:
            speak("Shutting down your PC")
            os.system("shutdown /s /f /t 5")
    
        elif "nahi" in query or "cancel" in query:
            speak("Shutdown cancelled")
            
        elif "cancel shutdown" in query:
            os.system("shutdown /a")
            speak("Shutdown cancelled successfully")
            
        elif "restart" in query:
            speak("Are you sure you want to restart?")
            query = takeCommand().lower()

        elif "yes" in query:
            speak("Restarting your PC")
            os.system("shutdown /r /f /t 5")
            
        elif "nahi" in query :
            speak("Restart cancel")
            