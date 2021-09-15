import subprocess
import time
from datetime import datetime

from watcher import watcher
from screen_maker import screen_maker


class account_manager(object):
    def __init__(self):
        self.log("account_manager ready")

    def log(self,info):
        now = datetime.now().time()
        now = str(now)
        print(now+" : "+info)
        

    