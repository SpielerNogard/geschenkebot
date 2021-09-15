import subprocess
import time
from datetime import datetime

from watcher import watcher
from screen_maker import screen_maker

class geschenke_annehmen(object):
    def __init__(self):
        self.log("geschenke_annehmen ready")
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

        self.open_all_presents()
        
        

        self.screen_maker.make_screen()
        self.close_menu()
        self.screen_maker.make_screen()
        self.close_menu()
        self.screen_maker.make_screen()

    def scroll(self):
        self.log("Scrolle")
        self.screen_maker.make_screen()
        subprocess.call("adb shell input swipe 100 1000 100 900 ",shell=True)
        time.sleep(8)
        self.screen_maker.make_screen()
        self.log("gescrollt")

    def open_all_presents(self):
        
        for a in range(10):
            self.look_for_presents()
            self.scroll()

    def open_present(self):
        self.screen_maker.make_screen()
        pos = self.Watcher.find_pos("geschenk")
        name = pos[0]
        coords = pos[1]
        val = pos[2]
        x = coords[0]
        y = coords[1]
        
        self.log("öffne Geschenk")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(8)
            self.open_present_ok()
        else:
            self.log("Konnte Geschenk öffnen")
            
    def open_present_ok(self):
        self.screen_maker.make_screen()
        pos = self.Watcher.find_pos("oeffnen")
        name = pos[0]
        coords = pos[1]
        val = pos[2]
        x = coords[0]
        y = coords[1]
        
        self.log("öffne Geschenk")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(20)
            self.log("geschenk geöffnet")
            #self.close_menu()
            
        else:
            self.log("Kein Open Button gefunden")
            

    def look_for_presents(self):
        self.screen_maker.make_screen()
        pos = self.Watcher.find_pos("geschenk_freund")
        name = pos[0]
        coords = pos[1]
        val = pos[2]
        x = coords[0]
        y = coords[1]
        
        self.log("suche nach Freunden mit Geschenken")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(8)
            self.open_present()
            self.close_menu()
        else:
            self.log("Konnte keine Geschenke finden")
            

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
        self.screen_maker.make_screen()
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
            #self.close_menu()
            



