from datetime import datetime


class geschenke_offner(object):
    def __init__(self):
        self.log("geschenke_offner ready")

    def log(self,info):
        now = datetime.now().time()
        now = str(now)
        print(now+" : "+info)
