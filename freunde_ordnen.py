import subprocess
import time
from datetime import datetime

from watcher import watcher
from screen_maker import screen_maker

class freunde_ordnen(object):
    def __init__(self):
        self.log("freunde_ordnen ready")
        self.screen_maker = screen_maker()
        self.Watcher = watcher()

    def log(self,info):
        now = datetime.now().time()
        now = str(now)
        print(now+" : "+info)

    def run(self):
        self.screen_maker.make_screen()
        self.offne_character()
        self.screen_maker.make_screen()
        self.ordnen()
        self.screen_maker.make_screen()

        self.screen_maker.make_screen()
        self.close_menu()
        self.screen_maker.make_screen()
        self.close_menu()
        self.screen_maker.make_screen()
        

    def offne_character(self):
        pos = self.Watcher.find_pos("character")
        name = pos[0]
        coords = pos[1]
        val = pos[2]
        x = coords[0]
        y = coords[1]
        
        self.log("Öffne Character")
        if val >= 0.7:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(10)
            self.log("Character geöffnet")
            self.log("Switche zu Freunde")
            subprocess.call("adb shell input swipe 400 200 100 200 ",shell=True)
            self.log("Freunde geöffnet")
            time.sleep(10)
        else:
            self.log("Konnte Character nicht finden")
            self.screen_maker.make_screen()
            self.offne_character()

    def close_menu(self):
        
        pos = self.Watcher.find_pos("freund_close")
        name = pos[0]
        coords = pos[1]
        val = pos[2]
        x = coords[0]
        y = coords[1]
        
        self.log("Schließe Menü")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(8)
            self.log("Menü geschlossen")
        else:
            self.log("Konnte Schließbutton nicht finden")

    def ordnen(self):
        
        pos = self.Watcher.find_pos("freunde_ordnen")
        name = pos[0]
        coords = pos[1]
        val = pos[2]

        x = coords[0]
        y = coords[1]
        
        self.log("Ordne Freunde")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(8)
            self.richtig_ordnen()
            
            
        else:
            self.log("Konnte Freunde nicht ordnen")
            self.close_menu()

    def richtig_ordnen(self):
        self.screen_maker.make_screen()
        pos = self.Watcher.find_pos("geschenk_ordnen")
        name = pos[0]
        coords = pos[1]
        val = pos[2]

        x = coords[0]
        y = coords[1]
        
        self.log("Ordne Freunde")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(8)
              
        else:
            self.log("Konnte Freunde nicht ordnen")
            
            



