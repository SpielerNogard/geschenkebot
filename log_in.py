import subprocess
import time
from datetime import datetime

from watcher import watcher
from screen_maker import screen_maker

class log_in(object):
    def __init__(self):
        self.log("log_out ready")
        self.screen_maker = screen_maker()
        self.Watcher = watcher()

    def log(self,info):
        now = datetime.now().time()
        now = str(now)
        print(now+" : "+info)

    def make_screen(self):
        self.screen_maker.make_screen()  

    def run(self,username,password):
        self.Username = username
        self.password = password
        self.screen_maker.make_screen()
        
        #processing returning
        #ptc
        #username
        #password
        #enter

        self.returning()
        self.ptc()
        self.login_with_ptc()

        self.screen_maker.make_screen()

    def login_with_ptc(self):
        self.input_username()
        self.press_somewhere()
        self.input_password()
        self.press_somewhere()
        self.einloggen()

    def press_somewhere(self):
        subprocess.call("adb shell input tap 600 500",shell=True)

    def input_username(self):
        self.make_screen()
        pos = self.Watcher.find_pos("username")
        name = pos[0]
        coords = pos[1]
        val = pos[2]

        x = coords[0]
        y = coords[1]
        
        self.log("Processing username")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(8)
            subprocess.call("adb shell input text '"+self.Username+"'",shell=True)
        else:
            self.log("Konnte username nicht finden")
            self.login_with_ptc()

    def ptc(self):
        self.make_screen()
        pos = self.Watcher.find_pos("ptc")
        name = pos[0]
        coords = pos[1]
        val = pos[2]

        x = coords[0]
        y = coords[1]
        
        self.log("Processing PTC")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(8)
            
        else:
            self.log("Konnte PTC nicht finden")
            self.ptc()

    def returning(self):
        self.make_screen()
        pos = self.Watcher.find_pos("returning")
        name = pos[0]
        coords = pos[1]
        val = pos[2]

        x = coords[0]
        y = coords[1]
        
        self.log("Processing Returning")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(8)
            
        else:
            self.log("Konnte Returning nicht finden")
            self.returning()

    def einloggen(self):
        self.make_screen()
        pos = self.Watcher.find_pos("anmelden")
        name = pos[0]
        coords = pos[1]
        val = pos[2]

        x = coords[0]
        y = coords[1]
        
        self.log("Eingeloggt")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(120)
            
            
        else:
            self.log("Konnte mich nicht einloggen")
            self.login_with_ptc()

    def input_password(self):
        self.make_screen()
        pos = self.Watcher.find_pos("password")
        name = pos[0]
        coords = pos[1]
        val = pos[2]

        x = coords[0]
        y = coords[1]
        
        self.log("Processing password")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(8)
            subprocess.call("adb shell input text '"+self.password+"'",shell=True)
        else:
            self.log("Konnte password nicht finden")
            self.login_with_ptc()


    



            



