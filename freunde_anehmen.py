import subprocess
import time
from datetime import datetime

from watcher import watcher
from screen_maker import screen_maker

class freunde_anehmen(object):
    def __init__(self):
        self.log("freunde_anehmen ready")
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
        self.search_for_requests()
        

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

    def search_for_requests(self):
        pos = self.Watcher.find_pos("friendrequests")
        name = pos[0]
        coords = pos[1]
        val = pos[2]
        x = coords[0]
        y = coords[1]
        
        self.log("Suche nach Anfragen")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(10)
            self.log("Anfragen geöffnet")
            for a in range(5):
                self.screen_maker.make_screen()
                self.anfragen_annehmen()
                self.screen_maker.make_screen()
        else:
            self.log("Keine Anfragen vorhanden")

    def anfragen_annehmen(self):
        pos = self.Watcher.find_pos("friendrequests_annehmen")
        name = pos[0]
        coords = pos[1]
        val = pos[2]
        x = coords[0]
        y = coords[1]
        
        self.log("Nehme Anfragen an")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(10)
            self.log("Anfragen angenommen")
        else:
            self.log("Keine Anfragen vorhanden")

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
            



