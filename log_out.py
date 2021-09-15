import subprocess
import time
from datetime import datetime

from watcher import watcher
from screen_maker import screen_maker

class log_out(object):
    def __init__(self):
        self.log("log_out ready")
        self.screen_maker = screen_maker()
        self.Watcher = watcher()

    def log(self,info):
        now = datetime.now().time()
        now = str(now)
        print(now+" : "+info)

    def run(self):
        self.screen_maker.make_screen()
        
        #menu öffnen
        self.öffne_menu()
        #einstellungen suchen und abmelden
        self.suche_einstellungen()
        self.screen_maker.make_screen()


    def abmelden(self):
        self.make_screen()
        pos = self.Watcher.find_pos("abmelden_ja")
        name = pos[0]
        coords = pos[1]
        val = pos[2]

        x = coords[0]
        y = coords[1]
        
        self.log("Logge aus")
        if val >= 0.8:
            self.log("Ausgeloggt")
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(40)
            
        else:
            self.log("Konnte Logout BEstätigung nicht finden")
            

    def logge_aus(self):
        self.make_screen()
        pos = self.Watcher.find_pos("abmelden")
        name = pos[0]
        coords = pos[1]
        val = pos[2]

        x = coords[0]
        y = coords[1]
        
        self.log("Logge aus")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(20)
            self.abmelden()
            
        else:
            self.log("Konnte Logout nicht finden")
            self.scroll()
            self.logge_aus()

    def make_screen(self):
        self.screen_maker.make_screen()  

    def suche_einstellungen(self):
        self.make_screen()
        pos = self.Watcher.find_pos("einstellungen")
        name = pos[0]
        coords = pos[1]
        val = pos[2]

        x = coords[0]
        y = coords[1]
        
        self.log("Öffne Einstellungen")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(10)
            self.make_screen()
            self.logge_aus()
        else:
            self.log("Konnte Einstellungen nicht finden")
            self.close_menu2()
            self.run()

    def scroll(self):
        self.log("Scrolle")
        self.screen_maker.make_screen()
        subprocess.call("adb shell input swipe 100 1000 100 800 ",shell=True)
        time.sleep(8)
        self.screen_maker.make_screen()
        self.log("gescrollt")
    
    def öffne_menu(self):
        self.make_screen()
        pos = self.Watcher.find_pos("menu")
        name = pos[0]
        coords = pos[1]
        val = pos[2]

        x = coords[0]
        y = coords[1]
        
        self.log("Öffne Menü")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(8)
            self.make_screen()
        else:
            self.log("Konnte Menu nicht finden")
            self.close_menu()

    def close_menu2(self):
        self.make_screen()
        pos = self.Watcher.find_pos("freund_close2")
        name = pos[0]
        coords = pos[1]
        val = pos[2]
        x = coords[0]
        y = coords[1]
        
        self.log("Schließe Menü")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(8)
            self.make_screen()
        else:
            self.log("Konnte Schließbutton nicht finden")
            #self.close_menu()

    def close_menu(self):
        self.make_screen()
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
            self.make_screen()
        else:
            self.log("Konnte Schließbutton nicht finden")
            #self.close_menu()



            



