import subprocess
import time
from datetime import datetime
from shutil import copyfile

class screen_maker(object):
    def __init__(self):
        self.log("screen_maker ready")

    def log(self,info):
        now = datetime.now().time()
        now = str(now)
        print(now+" : "+info)

    def make_screen(self):
        now = datetime.now().time()
        now = str(now)
        self.log("Mache Screenshot")
        subprocess.call("adb exec-out screencap -p > Bilder/screen.jpg",shell=True)
        now = now.replace(":","_")
        now = now.replace(".","_")
        copyfile("Bilder/screen.jpg","Bilder/"+str(now)+".jpg")
        self.log("Screenshot Saved")
        
    def run(self):
        while True:
            self.make_screen()


#BOBB = screen_maker()
#BOBB.run()