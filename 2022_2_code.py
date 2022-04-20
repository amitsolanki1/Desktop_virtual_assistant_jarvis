import datetime
from dis import Bytecode
import os
import random
import sys
import webbrowser as wb
from time import sleep
from plyer import notification
import smtplib
import PyPDF2
import keyboard
from requests import get
import instaloader
import psutil
import pyautogui
import pyjokes
import pyttsx3
import subprocess
import speedtest
from bs4 import BeautifulSoup
import pywhatkit as kit
import speech_recognition as sr
import wikipedia
from playsound import playsound
import calendar
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from jarvis2022_2 import Ui_jarvisui
from multiprocessing import Process

engine = pyttsx3.init()
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)
newvoicerate=180
engine.setProperty('rate',newvoicerate)
#engine.say("hello world")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#speak("hello ")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        # print("run")
        self.maincode()

    def time(self):
        #Time=datetime.datetime.now().strftime("%I:%M:%S")
        Time= datetime.datetime.now().strftime("%I:%M %p")
        speak("the current Time is")
        print(Time)
        speak(Time)

    def date(self):
        import time
        Year=int(datetime.datetime.now().year)
        # Month=int(datetime.datetime.now().month)
        date=int(datetime.datetime.now().day)
        m=time.strftime("%B")
        speak(f"Today's date is: {date} and it's {m} {Year} ")
        # tt=time.strftime("%A:%d:%B%Y")
        # print(tt)
        # speak(tt)

    def wishme(self):

        # speak("initializing the system")
        # speak("Starting all systems applications")
        # speak("Installing and checking all driver and hardware")
        # speak("caliberating and exmamining all the core processors")
        # speak("checking the internet connection")
        # speak("wait a moment sir")
        # speak("All drivers are up and running")
        # speak("All systems have been activated")
        # speak("Now i am online")
        # speak("I am jarvis virtual A I Assistant. Online and ready sir. Please tell me how may i help you")

        # speak("Welcome back Amit sir!")

        # playsound("arnold_audio\\Jarvis Start Up.wav")
        hour = datetime.datetime.now().hour
        Time = datetime.datetime.now().strftime("%I:%M %p")

        if hour >=0 and hour<=12:
            print(f"Good Morning Sir ,its {Time}")
            speak(f"Good Morning Sir, its {Time}")
        elif hour >=12 and hour <=18:
            print(f"Good Afternoon ,Sir its {Time}")
            speak(f"Good Afternoon ,its {Time}")
        else:
            print(f"Good Evening Sir ,its {Time}")
            speak(f"Good Evening Sir ,its {Time}")
    
    def youtubeautomation(self):
        self.query= self.takecommand().lower()
        if "skip" in self.query or "forward " in self.query:
            pyautogui.press('l')
        elif "back" in self.query or "backward " in self.query:
            pyautogui.press('j')
        elif "restart " in self.query:
            pyautogui.press('O')
        elif "pause " in self.query:
            pyautogui.press('space bar')
        elif "resume" in self.query:
            pyautogui.press('space bar')
        elif "full screen " in self.query:
            pyautogui.press('f')
        elif "film mode" in self.query:
            pyautogui.press('t')
        elif "increase" in self.query or "volume increase":
            pyautogui.hotkey('shift','.')
        elif "decrease" in self.query or "low" in self.query or "volume low" in self.query:
            pyautogui.hotkey('shift',',')
        elif "previous " in self.query:
            pyautogui.hotkey('shift','p')
        elif "next" in self.query or "play next" in self.query:
            pyautogui.hotkey('shift','n')
        elif "search " in self.query:
            pyautogui.click(x=667,y=146)
            speak("what to search")
            search= self.takecommand()
            pyautogui.typewrite(search)
            pyautogui.press('enter')

        elif "mute" in self.query or "volume mute" in self.query:
            pyautogui.press('m')
        elif "unmute" in self.query or "volume unmute"in self.query:
            pyautogui.press('m')
        elif 'bye'in self.query or "go" in self.query:
            exit()
            #sys.exit()

    def temperature(self):
        # import bs4 #pip install beautifulsoup4
        from bs4 import BeautifulSoup
        search = "temperature in delhi"
        url = f"https://www.google.com/search?q={search}"
        r= get(url)
        data= BeautifulSoup(r.text,"html.parser")
        temperature= data.find("div",class_="BNeawe").text
        print(f"the temperature outside is {temperature} celcius")
        speak(f"the temperature outside is {temperature} celcius")

        speak("do you i have to tell you another place temperature ?")
        next = self.takecommand()
        if "yes" in next:
            speak("tell me the name of the place")
            name = self.takecommand()
            search= search =f"temperature in {name}"
            url= f"https://www.google.com/search?q={search}"
            r=get(url)
            data =BeautifulSoup(r.text,"htnl.parser")
            temperature= data.find("div",class_="BNeawe").text
            speak(f"the temperature in {name} is {temperature} degree celcius")
        else:
            pass

    def chromeauto(self):
        while True:
            self.query = self.takecommand().lower()

            #self.query=input("hello")
            if"new tab" in self.query or "open new tab " in self.query:
                pyautogui.hotkey('ctrl','t')
            elif"close tab" in self.query or "close this tab " in self.query:
                pyautogui.hotkey('ctrl','w')
            elif"new window" in self.query or "open new window " in self.query:
                pyautogui.hotkey('ctrl','n')
            elif"history" in self.query or "show me history " in self.query:
                pyautogui.hotkey('ctrl','h')
            elif "download" in self.query or "show me downlaod " in self.query:
                pyautogui.hotkey('ctrl', 'j')
            elif "bookmarks" in self.query or "crate bookmarks " in self.query:
                pyautogui.hotkey('ctrl','d')
            elif "incognito mode" in self.query:
                keyboard.press_and_release('ctrl+shift+n')
                # pyautogui.hotkey('ctrl', 'shift','n')
            elif "restore tabs" in self.query or "restore " in self.query:
                keyboard.press_and_release('ctrl+shift+t')

            elif "switch tab" in self.query or "switch the tab" in self.query:
                pyautogui.keyDown('ctrl')
                pyautogui.press('tab')
                sleep(0.2)
                pyautogui.keyUp('ctrl')

            elif "break" in self.query or "bye" in self.query or "exit" in self.query:
                sys.exit()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone()as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)#,timeout=1,phrase_time_limit=5)
        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio,language='en-in')
            print(  f"you said: {self.query}")
        except Exception as e:
            print(e)
            #speak("Say that again please..")
            # return "none"

            self.query=input("enter your command: ")
            # self.query=self.ui.text.text()

        return self.query

    def sendmail(self,to,content):
        # noinspection PyUnresolvedReferences
        server =smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login("jaibholeki701@gmail.com","8527744381")
        server.sendmail("jaibhokeki701@gmail.com",to,content)
        server.close()

    def pdfreader(self):
        book = open('bookname.pdf','rb')
        reader= PyPDF2.PdfFileReader(book)
        pages= pdfReader.numPages
        speak(f"Total numbers of pages in this book  {pages}")
        speak("sir olease enter page number i have to read")
        pagenumber=int(input("enter page number:"))
        page= pdfReader.getPages(pagenumber)
        text= page.extractText()
        speak("sir i am start to read this book wait a second")
        speak(text)

    def youtube_video_downloader(self):
        from pytube import YouTube
        speak("enter url of video ")
        link =input("Enter URL of Youtube video here..")
        url_of_video=YouTube(link)
        s=url_of_video.streams.first()
    #download video in highest resolution 
    # s=url_of_video.streams.get_highest_resolution()
        speak("sir video is downloading.. wait few seconds")
        s.downlaod()
        print("done sir")

        speak("done sir")
    
    def setalarm(self,text):
        import alarm
        with open("alarm.txt",'a')as f:
            f.write(text)
            f.close()
        speak("sir alarm is set")
        alarm.alarm(text)
        os.startfile("alarm.py")
    def screenshot(self):
        speak("Tell me the name for this screenshot file")
        name=self.takecommand().lower()
        name=input()
        speak("taking screenshot")
        img= pyautogui.screenshot()
        img.save(f"C:\\Users\\abc\\Music\\{name}.png")
        speak("done sir")
    def cpu(self):
        usage= str(psutil.cpu_percent())
        speak(f"CPU is at { usage } percent usage")
    def batteryb(self):
        battery = psutil.sensors_battery()
        
        speak(f"sir our system have {battery.percent} percent battery")
    def jokes(self):
        print(pyjokes.get_joke())
        speak(pyjokes.get_joke())

    def maincode(self):

        self.wishme()
        notification.notify(title="Start ",
                            message="I am online and ready to do task ",
                            app_icon=None,
                            timeout=3)
        # playsound("arnold_audio\powerup.mp3")

        battery = psutil.sensors_battery()
        plug=battery.power_plugged
        bb=battery.percent
        while True:

            #from win10 import 
            if plug==True:
                notification.notify(title="Charging",
                                    message=f"Battery chargeing wait sometime to fill the battery,{bb}% battery remain!!",
                                    app_icon=None,
                                    timeout=5)
            if bb >20 and bb <=30 :
                notification.notify(title="battery",
                                    message=f"battery status low please charge {bb} ",
                                    app_icon=None,
                                    timeout=2)
                speak(f'sir battery low , charge me its {bb} percent battery')
            elif bb>=12 and bb<=20:
                notification.notify(title="Danger!! LOW Battery",
                                    message=f"battery status low please charge and Remainig battery is {bb} ",
                                    app_icon='battery.ico', #always use ico file
                                    timeout=2)
                speak(f"we have very low power, please connect to charging the system will shutdown very soon")
            elif bb ==11 :
                speak(f'sir battery low,  please charge me we have very low power its {bb} percent battery')

            # self.query = self.takecommand().lower() or input("enter command: ")
            self.query=input("Listing...")
            #self.query = input("eneter command")
            print(self.query)
            
            
            if "time" in self.query or "tell me the time"in self.query:
                self.time()
            elif "date" in self.query or "current date" in self.query:
                self.date()

            elif"calendar"in self.query or "show me calendar" in self.query:
                import calendar
                c=calendar.TextCalendar().formatyear(2021)
                speak("sir now calendar are display on console you can go and check")
                print("sir now calendar are display on console you can go and check")
                print(c)

            elif "wikipedia" in self.query:
                speak("Searching...")
                self.query= self.query.replace("wikipedia","")
                result= wikipedia.summary(self.query,sentences = 2)
                print(result)
                speak(result)
            elif "sendmail" in self.query:
                try:
                    speak("what should i say?")
                    content=self.takecommand()
                    to="amit100lanki701@gmail.com"
                    self.sendmail(to,content)
                    speak("email send sucessfully")
                except Exception as e:
                    speak(e)
                    print(e)
                    speak("unable to send the email")
            elif "search in chrome" in self.query:
                speak("what should i search?")
                chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                search= self.takecommand().lower()
                wb.get(chromepath).open_new_tab(search+".com")

            elif "shutdown" in self.query or "shutdown the system" in self.query:
                os.system("shutdown /s /t 5")
            elif "logout" in self.query or "logout the system" in self.query:
                os.system("shutdown /r /t 5")
            elif "restart" in self.query or "restart the system" in self.query:
                os.system("shutdown /r /t 5")
            elif "sleep" in self.query or "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif "music" in self.query or "play music" in self.query:
                song_dir = "F:\\music\\new"
                songs= os.listdir(song_dir)
                rd= random.choice(songs)
                os.startfile((os.path.join(song_dir,rd)))
                #os.startfile(os.path.join(song_dir,songs[0]))
            elif "video" in self.query or "play video" in self.query:
                video_dir = "F:\\video"
                video= os.listdir(video_dir)
                rd= random.choice(video)
                os.startfile((os.path.join(video_dir,rd)))
                #os.startfile(os.path.join(song_dir,songs[0]))

            elif "play online music" in self.query or "play music online" in self.query:
                song = self.query.replace("play","")
                speak("playing..."+song)
                try:
                    kit.playonyt(song)
                except Exception as e:

                    print(e)

            elif "remember that" in self.query:
                speak("what should i remember?")
                data = self.takecommand()
                speak("you said me to remember" + data)
                remember = open("data.txt","w")
                remember.write(data)
                remember.close()
            elif "do you remember anything" in self.query:
                remember = open("data.txt","r")
                speak("you said me to remember that" + remember.read())
            elif "screenshot" in self.query or "ss" in self.query or "take a screenshot" in self.query:
                self.screenshot()
            elif "cpu" in self.query:
                self.cpu()
            elif "battery status" in self.query or "how much power left" in self.query:
                self.batteryb()
            elif "joke" in self.query or "tell me a joke" in self.query:
                self.jokes()

            # elif "tell me internet speed" or "what is my internet speed" in self.query:
            #     st= speedtest.Speedtest()
            #     d=st.download()
            #     dinmb=d/8000000
            #     up=st.upload()
            #     upinmb=up/8000000
            #     #speak(f"sir we have {d} bits per second downlading speed")
            #     #speak(f"and {up} bit per second uploading speed")
            #     speak(f"sir we have {dinmb} M B per second downloading speed")
            #     speak(f"and {upinmb} M B per second uploading speed")

            # elif"speed" in self.query:
            #     try:
            #         os.system('cmd /k "speedtest"')
            #     except:
            #         speak("error")

            #webbrowser
            elif "open facebook" in self.query or "facebook" in self.query:
                wb.open("https://www.facebook.com")
            elif "open olx" in self.query or "olx" in self.query:
                wb.open("https://www.olx.in")
            elif "open google" in self.query or "google" in self.query:
                wb.open("https://www.google.com")
            elif "open ebay" in self.query or "ebay" in self.query:
                wb.open("https://www.ebay.com")
            elif "open twitter" in self.query or "twitter" in self.query:
                wb.open("https://www.twitter.com")

            elif "open amazon" in self.query or "amazon" in self.query:
                wb.open("https://www.amazon.in")
            elif "open flipkart" in self.query or "flipkart" in self.query:
                wb.open("https://www.flipkart.com")
            elif "open instagram" in self.query or "instagram" in self.query:
                wb.open("https://www.instagram.com")
            elif "open youtube" in self.query or "youtube" in self.query:
                wb.open("https://www.youtube.com")
                self.youtubeautomation()
            elif "open stackoverflow" in self.query or "stackoverflow" in self.query:
                wb.open("https://www.stackoverflow.com")
            elif "open investing" in self.query or "investing" in self.query:
                wb.open("https://www.investing.com")
            elif "open gmail" in self.query or "gmail" in self.query:
                wb.open("https://www.gmail.com")
            #apps
            elif"open chrome" in self.query or "chrome" in self.query:
                path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                speak("opening Chrome")
                os.startfile(path)
        
            elif"open vscode" in self.query or "vscode" in self.query:
                path = "C:\\Program Files\\Microsoft VS Code\\code.exe"
                speak("opening Chrome")
                os.startfile(path)
        
            elif "open command prompt" in self.query or "cmd" in self.query or "open cmd" in self.query:
                speak("opening CMD")
                os.system("start cmd")
            elif "open notepad" in self.query or "notepad" in self.query:
                path = "C:\\WINDOWS\\system32\\notepad.exe"
                speak("opening Notepad")
                os.startfile(path)

            #close apps
            elif "close chrome" in self.query or "chrome close" in self.query:
                os.system("taskkill /f /im chrome.exe")
            elif "close cmd" in self.query:
                speak("ok sir, closing... cmd")
                os.system("TASKKILL /f /im cmd.exe")

            elif "close notepad" in self.query:
                speak("ok sir, closing...notepad")
                os.system("TASKKILL /f /im notepad.exe")
            elif"close vscode" in self.query:
                speak("ok sir , closing .. vscode")
                os.system("taskkill /f /im code.exe")

            #computer automation

            elif "open mobile camera" in self.query or "mobile camera" in self.query:

                import urllib.request
                from cv2 import imdecode,imshow,waitKey,destroyAllWindows  #pip install opencv-python
                from numpy import array,uint8 #pip install numpy
                url="http://192.168.43.1:8080/shot.jpg"
                while True:
                    img_array=array(Bytecode(urllib.request.urlopen(url).read(),dtype=uint8))
                    img=imdecode(img_array,-1)
                    imshow("IPWEB_CAM",img)
                    if waitKey(1)==ord('q'):
                        break
                destroyAllWindows()

            elif "send message" in self.query:
                speak("what should i say")
                msg=self.takecommand().lower()
                from twilio.rest import Client  #pip install twilio
                account_sid=""
                auth_token=""
                client=Client(account_sid,auth_token)
                message=client.messages \
                    .create(
                        body=msg,
                        from_="+91",
                        to="+919910628828"
                    )
                print(message.sid)

            elif "make a call" in self.query or "call" in self.query:
                # msg=self.takecommand().lower()
                from twilio.rest import Client  #pip install twilio
                account_sid=""
                auth_token=""
                client=Client(account_sid,auth_token)
                message=client.calls \
                    .create(
                        twiml='<Response><Say>This is the teseting message from jarvis</Say></Response>',
                        from_="+919910628828",
                        to="+919910628828"
                    )
                print(message.sid)

            elif "open my computer" in self.query or "my computer" in self.query:
                speak("opening my computer...")
                pyautogui.hotkey('win','e')
            elif "open setting" in self.query:
                speak("open settings")
                pyautogui.hotkey('win', 'i')
            elif "show display setting" in self.query or "display setting" in self.query:
                pyautogui.hotkey('win', 'u')
            elif "show start" in self.query:
                pyautogui.press('win')
            elif "minimize" in self.query or "desktop" in self.query:
                pyautogui.hotkey('win','m')
            elif "maximize" in self.query or "restore window" in self.query:
                #pyautogui.hotkey('win','shift','m')
                pyautogui.hotkey('win','d')
            elif "open search" in self.query or "search" in self.query:
                pyautogui.hotkey('win','s')

            elif "magnifier" in self.query:
                pyautogui.hotkey('ctrl','+')

            elif "show magnifier" in self.query:
                keyboard.press_and_release('ctrl+win+m')
            elif "volume up" in self.query:
                pyautogui.press('volumeup')
            elif "volume down" in self.query:
                pyautogui.press('volumedown')
            elif "mute" in self.query:
                pyautogui.press('volumemute')
            elif "what is my ip" in self.query:
                speak("wait sir, let me check")
                ip = get('https://api.ipify.org').text
                print(ip)
                speak(ip)

            elif"where i am" in self.query or "tell me my location" in self.query or "where we are" in self.query:
                speak("wait sir, let me check")
                try:
                    ip=get('https://api.ipify.org').text
                    print(ip)
                    url= 'https://get.geojs.io/v1/ip/geo/'+ip+'.json'
                    geo_request= get(url)
                    geo_data=geo_request.json()
                    #print(geodata)
                    city= geo_data['city']
                    #state =geo_data['state']
                    country =geo_data['country']
                    print(f"sir i am not sure ,but i think we are in {city} city of {country} country")
                    speak(f"sir i am not sure ,but i think we are in {city} city of {country} country")
                    
                except Exception as e:
                    print("sorry sir ,due to network issue i am not abke to find where we are")
                    pass
            elif "tell me temperature" in self.query or "what is the temperature" in self.query:
                speak("wait sir, let me check")
                self.temperature()

            elif "instagram profile" in self.query or "show instagram profile" in self.query:
                speak("sir please enter the user name correctly")
                name = input("enter username :")
                wb.open(f"www.instagram.com/{name}")
                speak(f"sir here is the profile of the user {name}")
                sleep(2)
                speak("sir would you like to download profile picture of the account.")
                usercondition = self.takecommand()

                if "yes" in usercondition:
                    mod= instaloader.Instaloader()
                    mod.download_profile(name,profile_pic_only=True)
                    speak("i am done sir! , profile picture is saved")
                else:
                    pass

            elif"locate" in self.query:
                speak("wait i sir")
                self.query=self.query.replace('locate ',"")
                url=f"https://googlemap.co.in/{self.query}"
                wb.open(url)
                

            elif "audio book" in self.query or "read book" in self.query:
                speak("reading book ")
                self.pdfreader()
            elif "set alarm" in self.query:
                self.setalarm(self.query)
            elif"camera" in self.query or "open camera"in self.query:
                speak("opening camera")
                subprocess.run("start microsoft.windows.camera:",shell=True)

            elif 'find location' in self.query or "show me the location of this number" in self.query :
                import phonenumbers
                from phonenumbers import geocoder,carrier,timezone
                speak("enter phone number to check location")
                number= input("enter phone number to check location: ")
                #ch_number=phonenumbers.parse("enter mobile number")
                ch_number= phonenumbers.parse(number,'CH')
                #print the country name
                print(geocoder.description_for_number(ch_number,"en"))
                #print the servie provider
                print(carrier.name_for_number(ch_number,"en"))
                #print the timezone
                print(timezone.time_zones_for_number(ch_number))
            
                serial_num=phonenumbers.parse(number,'RO')
                print(carrier.name_for_number(serial_num,"en"))
            
            elif"video downloader" in self.query or "youtube video downlaod" in self.query:
                speak("wait sir")
                self.youtube_video_downloader()

            elif"activate how to do mode" in self.query or "how to do mode" in self.query:
                #from pywikihow import search_wikihow
                speak("How to do mode in activated please tell me what you want to how ")
                tell=self.takecommand()
                max_result =1
                how_to= search_wikihow(tell,max_result)
                assert len(how_to) ==1
                how_to[0].print()
                speak(how_to[0].summary)

            elif "exit" in self.query or "gooffline" in self.query or "go offline" in self.query:
                speak("ok sir!!")
                speak("closing all system application")
                speak("disconectiong to server")
                #speak("disconnecting to internet")
                speak("i am going offline")
                playsound("arnold_audio\\power down.mp3")
                sys.exit()

            elif "visible all files" in self.query or "visible this folder" in self.query:
                os.system("attrib -h /s /d")
                speak("sir , all the files in this folder are now visible to everyone")
            elif 'calc' in self.query :
                from cal import Ui_MainWindow 
                app = QtWidgets.QApplication(sys.argv)
                MainWindow = QtWidgets.QMainWindow()
                ui = Ui_MainWindow()
                ui.setupUi(MainWindow)
                MainWindow.show()
                sys.exit(app.exec_())

            elif "switch" in self.query or "switch the window"in self.query:
                pyautogui.hotkey('alt','tab')
            elif "create new folder" in self.query:
                pyautogui.hotkey('ctrl','shiftleft','n')
        
            elif "hide all files" in self.query or "secure this folder" in self.query:
                os.system("attrib +h /s /d")
                speak("sir , all the files in this folder are now hidden")

            # elif "switch the window" or "switch" in self.query:
            #     pyautogui.keyDown("alt")
            #     pyautogui.press("tab")
            #     sleep(0.2)
            #     pyautogui.keyUp("alt")

            elif "fun" in self.query or "lets do fun" in self.query:
                wb.open("https://www.youtube.com/feed/trending")
            else:
                var= self.query.replace(' '," ")
                url= f"https://www.google.com/search?q=+{var}"
                speak("sorry sir i can't understand but i searchfrom internet to give your answer? okay")
                speak("wait a few second")
                wb.open(url)

# instance of mainThread class
startfirstclass=MainThread()

class Main(QMainWindow,):
    def __init__(self):
        super().__init__()
        self.ui=Ui_jarvisui()
        self.ui.setupUi(self)
        self.ui.start.clicked.connect(self.startbtn)
        self.ui.pushButton.clicked.connect(self.close)

    def startbtn(self):
        timer =QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)

        self.ui.movie=QtGui.QMovie("E:/project/PYTHON/UI/ui/gif/initial.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("E://project//PYTHON//UI//ui//gif//jarvis_jj.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("E:/project/PYTHON/UI/ui/gif/loading_1.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("E:/project/PYTHON/UI/ui/gif/Earth_Template.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.moive=QtGui.QMovie("E:/project/PYTHON/UI/ui/robot.gif")
        self.ui.label_8.setMovie(self.ui.moive)
        self.ui.moive.start()
        self.ui.moive=QtGui.QMovie("E:/project/PYTHON/UI/ui/gif/Code_Template.gif")
        self.ui.label_9.setMovie(self.ui.moive)
        self.ui.moive.start()
        self.ui.movie=QtGui.QMovie("E:/project/PYTHON/UI/ui/gif/Ntuks.gif")
        self.ui.label_12.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("E:/project/PYTHON/UI/ui/gif/Siri.gif")
        self.ui.label_14.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("ui/gif/Aqua.gif")
        self.ui.label_21.setMovie(self.ui.movie)
        self.ui.movie.start()


        startfirstclass.start()
        
        battery_info=psutil.sensors_battery()
        print(battery_info)
        print("battery percent: ",battery_info.percent)
        battery_left=battery_info.secsleft
        battery_left=round((battery_left/60)/60,2)
        print("battery left:",battery_left)
        # battery_left_hours=battery_left
        # battery_left_min=battery_left[1:]
        # print(battery_left_hours)
        # print(battery_left_min)
        plugged=battery_info.power_plugged


        # r = sr.Recognizer()
        # with sr.Microphone()as source:
        #     print("Listening...")
        #     self.ui.textBrowser.setText("Listening..")
        #     r.pause_threshold = 1
        #     audio = r.listen(source)#,timeout=1,phrase_time_limit=5)

        # try:
        #     print("Recognizing...")
        #     self.ui.textBrowser.setText("Recognizing..")
        #     self.query = r.recognize_google(audio,language='en-in')
        #     print(f"you said: {self.query}")
        # except Exception as e:
        #     print(e)
        #     #speak("Say that again please..")
        #     # return "none"
        #     self.ui.textBrowser.setText("Recognizing error!!")
            
        #     self.query=input("enter your command: ")
        #     # self.query=self.ui.text.text()
# white input box
        # input_=self.ui.text.text()
        # print(input_)    


        if plugged:
            self.ui.charging.setText(str("Plugged"))
        else:
            self.ui.charging.setText(str("Not Plugged"))
        self.ui.battery.setText(str(battery_left)+str("Hours left!"))
        self.ui.label_20.setText(str(battery_info.percent)+str("%"))
    #show memory ,diskspace
        cpu_=psutil.cpu_percent()
        # while True:
        disk_usage=psutil.disk_usage(os.sep).percent
        print(disk_usage)
        cpu_count_=psutil.cpu_count()
        a=psutil.disk_partitions()
        # b=psutil.disk_usage('/')
        print(a)
        a=a[0]
        print(a)
        print(a[1])
        print(psutil.swap_memory())
        s=psutil.swap_memory()
        s=s.percent
        #virtual memory
        vm=psutil.virtual_memory().percent
        # self.progressBar=QProgressBar(self)
        # self.ui.progressBar.setGeometry(45,45,500,500)
        self.ui.progress_label.setText("SYSTEM USES")
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(cpu_)
        self.ui.progres_label_text.setText("CPU USAGES")
        self.ui.progressbar_label1.setText(str(cpu_)+str("%"))
        self.ui.progressBar_2.setValue(vm)
        self.ui.progress_label_text1.setText("VIRTUAL MEMORY")
        self.ui.progressbar_label2.setText(str(vm)+str("%"))
        self.ui.progressBar_4.setValue(s)
        self.ui.progress_label_text3.setText("SWAP MEMORY")
        self.ui.progressbar_label4.setText(str(s)+str("%"))
        
        self.ui.progress_label_text4.setText("DISK USAGES")
        self.ui.progressBar_5.setValue(disk_usage)
        self.ui.progressbar_label5.setText(str(disk_usage)+str("%") )

        # disk usages
        # self.ui.disk.setText("Disk usages ")
        # self.ui.progressBar_disk.setValue(disk_usage)
        # self.ui.disk_label.setText(str(disk_usage))

        disk_operation=psutil.disk_io_counters()
        write_operation=disk_operation[1]
        read_operation=disk_operation[0]
        print("disk operation ",disk_operation)
        print("write operation",write_operation)
        print("read operation",read_operation)
        # self.ui.progressBar_disk.setValue(write_operation)
        #available memory 
        mem=psutil.virtual_memory()
        mem_percent=mem.percent
        mem_used=round(mem.used,2)

        # mem_free=round(mem.free/800000)
        memory_free_in_gb=round(mem.free/1073741824,2)

        print("memory free in gb: ",memory_free_in_gb)

        ttl=mem.total  #show total memory
        THRESHOLD=500 * 1024 * 1024  # 500MB
        if mem.available>=THRESHOLD:
            # sleep(2)
            # speak("... warning virtual memrory is low...")
            print("warning memrory is low")

        total_memory_in_gb=round(ttl/1073741824,3)
        print("total memory in GB: ",total_memory_in_gb)
        self.ui.progressBar_3.setMaximum(8)
        self.ui.progress_label_text2.setText("RAM FREE")
        self.ui.progressBar_3.setValue(memory_free_in_gb)
        self.ui.progressbar_label3.setText(str(memory_free_in_gb*10)+str("%"))

        # show calendar
        year=datetime.datetime.now().year
        month=datetime.datetime.now().month
        day=datetime.datetime.now().day
        c=calendar.TextCalendar().formatmonth(year,month)
        self.ui.label_13.setText(c)
        if str(day) in str(self.ui.label_13) :
            self.ui.label_13.setStyleSheet("background:red;")
            print("find")

        # m1=Process(self.multi_threading())   
        # m1.start()    
    # def multi_threading(self):
        
#         battery_info=psutil.sensors_battery()
#         print(battery_info)
#         print("battery percent: ",battery_info.percent)
#         battery_left=battery_info.secsleft
#         battery_left=round((battery_left/60)/60,2)
#         print("battery left:",battery_left)
#         # battery_left_hours=battery_left
#         # battery_left_min=battery_left[1:]
#         # print(battery_left_hours)
#         # print(battery_left_min)
#         plugged=battery_info.power_plugged


#         # r = sr.Recognizer()
#         # with sr.Microphone()as source:
#         #     print("Listening...")
#         #     self.ui.textBrowser.setText("Listening..")
#         #     r.pause_threshold = 1
#         #     audio = r.listen(source)#,timeout=1,phrase_time_limit=5)

#         # try:
#         #     print("Recognizing...")
#         #     self.ui.textBrowser.setText("Recognizing..")
#         #     self.query = r.recognize_google(audio,language='en-in')
#         #     print(f"you said: {self.query}")
#         # except Exception as e:
#         #     print(e)
#         #     #speak("Say that again please..")
#         #     # return "none"
#         #     self.ui.textBrowser.setText("Recognizing error!!")
            
#         #     self.query=input("enter your command: ")
#         #     # self.query=self.ui.text.text()
# # white input box
#         input_=self.ui.text.text()
#         print(input_)    
#         if plugged:
#             self.ui.charging.setText(str("Plugged"))
#         else:
#             self.ui.charging.setText(str("Not Plugged"))
#         self.ui.battery.setText(str(battery_left)+str("Hours left!"))
#         self.ui.label_20.setText(str(battery_info.percent)+str("%"))
#     #show memory ,diskspace
#         cpu_=psutil.cpu_percent()
#         # while True:
#         disk_usage=psutil.disk_usage(os.sep).percent
#         print(disk_usage)
#         cpu_count_=psutil.cpu_count()
#         a=psutil.disk_partitions()
#         # b=psutil.disk_usage('/')
#         print(a)
#         a=a[0]
#         print(a)
#         print(a[1])
#         print(psutil.swap_memory())
#         s=psutil.swap_memory()
#         s=s.percent
#         #virtual memory
#         vm=psutil.virtual_memory().percent
#         # self.progressBar=QProgressBar(self)
#         # self.ui.progressBar.setGeometry(45,45,500,500)
#         self.ui.progress_label.setText("SYSTEM USES")
#         self.ui.progressBar.setMaximum(100)
#         self.ui.progressBar.setValue(cpu_)
#         self.ui.progres_label_text.setText("CPU USAGES")
#         self.ui.progressbar_label1.setText(str(cpu_)+str("%"))
#         self.ui.progressBar_2.setValue(vm)
#         self.ui.progress_label_text1.setText("VIRTUAL MEMORY")
#         self.ui.progressbar_label2.setText(str(vm)+str("%"))
#         self.ui.progressBar_4.setValue(s)
#         self.ui.progress_label_text3.setText("SWAP MEMORY")
#         self.ui.progressbar_label4.setText(str(s)+str("%"))
        
#         self.ui.progress_label_text4.setText("DISK USAGES")
#         self.ui.progressBar_5.setValue(disk_usage)
#         self.ui.progressbar_label5.setText(str(disk_usage)+str("%") )

#         # disk usages
#         # self.ui.disk.setText("Disk usages ")
#         # self.ui.progressBar_disk.setValue(disk_usage)
#         # self.ui.disk_label.setText(str(disk_usage))

#         disk_operation=psutil.disk_io_counters()
#         write_operation=disk_operation[1]
#         read_operation=disk_operation[0]
#         print("disk operation ",disk_operation)
#         print("write operation",write_operation)
#         print("read operation",read_operation)
#         #available memory 
#         mem=psutil.virtual_memory()
#         mem_percent=mem.percent
#         mem_used=round(mem.used,2)

#         # mem_free=round(mem.free/800000)
#         memory_free_in_gb=round(mem.free/1073741824,2)

#         print("memory free in gb: ",memory_free_in_gb)

#         ttl=mem.total  #show total memory
#         THRESHOLD=500 * 1024 * 1024  # 500MB
#         if mem.available>=THRESHOLD:
#             # sleep(2)
#             # speak("... warning virtual memrory is low...")
#             print("warning memrory is low")

#         total_memory_in_gb=round(ttl/1073741824,3)
#         print("total memory in GB: ",total_memory_in_gb)
#         self.ui.progressBar_3.setMaximum(8)
#         self.ui.progress_label_text2.setText("RAM FREE")
#         self.ui.progressBar_3.setValue(memory_free_in_gb)
#         self.ui.progressbar_label3.setText(str(memory_free_in_gb)+str("%"))

#         # show calendar
#         year=datetime.datetime.now().year
#         month=datetime.datetime.now().month
#         day=datetime.datetime.now().day
#         c=calendar.TextCalendar().formatmonth(year,month)
#         self.ui.label_13.setText(c)
#         if str(day) in str(self.ui.label_13) :
#             self.ui.label_13.setStyleSheet("background:red;")
#             print("find")

#         while True:
#             sleep(10)
#             battery_info=psutil.sensors_battery()
#             print(battery_info)
#             print("battery percent: ",battery_info.percent)
#             battery_left=battery_info.secsleft
#             battery_left=round((battery_left/60)/60,2)
#             print("battery left:",battery_left)
#             # battery_left_hours=battery_left
#             # battery_left_min=battery_left[1:]
#             # print(battery_left_hours)
#             # print(battery_left_min)
#             plugged=battery_info.power_plugged


#             # r = sr.Recognizer()
#             # with sr.Microphone()as source:
#             #     print("Listening...")
#             #     self.ui.textBrowser.setText("Listening..")
#             #     r.pause_threshold = 1
#             #     audio = r.listen(source)#,timeout=1,phrase_time_limit=5)

#             # try:
#             #     print("Recognizing...")
#             #     self.ui.textBrowser.setText("Recognizing..")
#             #     self.query = r.recognize_google(audio,language='en-in')
#             #     print(f"you said: {self.query}")
#             # except Exception as e:
#             #     print(e)
#             #     #speak("Say that again please..")
#             #     # return "none"
#             #     self.ui.textBrowser.setText("Recognizing error!!")
                
#             #     self.query=input("enter your command: ")
#             #     # self.query=self.ui.text.text()
#     # white input box
#             input_=self.ui.text.text()
#             print(input_)    
#             if plugged:
#                 self.ui.charging.setText(str("Plugged"))
#             else:
#                 self.ui.charging.setText(str("Not Plugged"))
#             self.ui.battery.setText(str(battery_left)+str("Hours left!"))
#             self.ui.label_20.setText(str(battery_info.percent)+str("%"))
#         #show memory ,diskspace
#             cpu_=psutil.cpu_percent()
#             # while True:
#             disk_usage=psutil.disk_usage(os.sep).percent
#             print(disk_usage)
#             cpu_count_=psutil.cpu_count()
#             a=psutil.disk_partitions()
#             # b=psutil.disk_usage('/')
#             print(a)
#             a=a[0]
#             print(a)
#             print(a[1])
#             print(psutil.swap_memory())
#             s=psutil.swap_memory()
#             s=s.percent
#             #virtual memory
#             vm=psutil.virtual_memory().percent
#             # self.progressBar=QProgressBar(self)
#             # self.ui.progressBar.setGeometry(45,45,500,500)
#             self.ui.progress_label.setText("SYSTEM USES")
#             self.ui.progressBar.setMaximum(100)
#             self.ui.progressBar.setValue(cpu_)
#             self.ui.progres_label_text.setText("CPU USAGES")
#             self.ui.progressbar_label1.setText(str(cpu_)+str("%"))
#             self.ui.progressBar_2.setValue(vm)
#             self.ui.progress_label_text1.setText("VIRTUAL MEMORY")
#             self.ui.progressbar_label2.setText(str(vm)+str("%"))
#             self.ui.progressBar_4.setValue(s)
#             self.ui.progress_label_text3.setText("SWAP MEMORY")
#             self.ui.progressbar_label4.setText(str(s)+str("%"))
            
#             self.ui.progress_label_text4.setText("DISK USAGES")
#             self.ui.progressBar_5.setValue(disk_usage)
#             self.ui.progressbar_label5.setText(str(disk_usage)+str("%") )

#             # disk usages
#             # self.ui.disk.setText("Disk usages ")
#             # self.ui.progressBar_disk.setValue(disk_usage)
#             # self.ui.disk_label.setText(str(disk_usage))

#             disk_operation=psutil.disk_io_counters()
#             write_operation=disk_operation[1]
#             read_operation=disk_operation[0]
#             print("disk operation ",disk_operation)
#             print("write operation",write_operation)
#             print("read operation",read_operation)
#             #available memory 
#             mem=psutil.virtual_memory()
#             mem_percent=mem.percent
#             mem_used=round(mem.used,2)

#             # mem_free=round(mem.free/800000)
#             memory_free_in_gb=round(mem.free/1073741824,2)

#             print("memory free in gb: ",memory_free_in_gb)

#             ttl=mem.total  #show total memory
#             THRESHOLD=500 * 1024 * 1024  # 500MB
#             if mem.available>=THRESHOLD:
#                 # sleep(2)
#                 # speak("... warning virtual memrory is low...")
#                 print("warning memrory is low")

#             total_memory_in_gb=round(ttl/1073741824,3)
#             print("total memory in GB: ",total_memory_in_gb)
#             self.ui.progressBar_3.setMaximum(8)
#             self.ui.progress_label_text2.setText("RAM FREE")
#             self.ui.progressBar_3.setValue(memory_free_in_gb)
#             self.ui.progressbar_label3.setText(str(memory_free_in_gb)+str("%"))

#             # show calendar
#             year=datetime.datetime.now().year
#             month=datetime.datetime.now().month
#             day=datetime.datetime.now().day
#             c=calendar.TextCalendar().formatmonth(year,month)
#             self.ui.label_13.setText(c)
#             if str(day) in str(self.ui.label_13) :
#                 self.ui.label_13.setStyleSheet("background:red;")
#                 print("find")

 
    def showtime(self):
        ct=QTime.currentTime()
        now=QDate.currentDate()
        labeltime=ct.toString("hh:mm:ss")
        labeldate=now.toString(Qt.ISODate)
        self.ui.textBrowser.setText(labeltime)
        self.ui.textBrowser_2.setText(labeldate)

    
app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())