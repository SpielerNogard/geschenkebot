import subprocess
import time
from datetime import datetime

from watcher import watcher
from screen_maker import screen_maker


class screen_checker(object):
    def __init__(self):
        self.log("screen_checker ready")
        self.screen_maker = screen_maker()
        self.Watcher = watcher()

    def log(self,info):
        now = datetime.now().time()
        now = str(now)
        print(now+" : "+info)

    def check_screen(self):
        self.log("Checke Screen")
        self.screen_maker.make_screen()
        self.check_for_warning()
        self.screen_maker.make_screen()
        self.check_for_info()
        self.screen_maker.make_screen()

    def check_for_warning(self):
        pos = self.Watcher.find_pos("ok")
        name = pos[0]
        coords = pos[1]
        val = pos[2]

        x = coords[0]
        y = coords[1]
        
        self.log("Suche nach Warnung")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(10)
            self.log("Warnung gefunden und geklickt")
            
            
        else:
            self.log("Konnte keine Warnung finden")
            
    def check_for_info(self):
        pos = self.Watcher.find_pos("ausblenden")
        name = pos[0]
        coords = pos[1]
        val = pos[2]

        x = coords[0]
        y = coords[1]
        
        self.log("Suche nach Informationen zum ausblenden")
        if val >= 0.8:
            subprocess.call("adb shell input tap "+str(x)+" "+str(y),shell=True)
            time.sleep(10)
            self.log("Informationen gefunden und geklickt")
            
            
        else:
            self.log("Konnte keine Informationen finden")

    def chek_for_lvl_up(self):
        pass
