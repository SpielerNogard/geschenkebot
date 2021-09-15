import cv2 as cv
import numpy as np
from datetime import datetime


class watcher(object):
    def __init__(self):
        self.templates = []
        self.template_names = ["abmelden","abmelden_ja","freunde_ordnen","beutel","character","einstellungen","freund_close","freund_close2","freunde","geschenk","geschenk_freund","geschenk_ordnen","ausblenden","friendrequests","friendrequests_annehmen","menu","mulleimer","oeffnen","anmelden","username","password","ptc","returning","ok","ja","more"]
        self.load_templates()

    def log(self,info):
        now = datetime.now().time()
        now = str(now)
        print(now+" : "+info)

    def load_templates(self):
        
        for Name in self.template_names:
            test = []
            test.append(Name)
            image = cv.imread("templates/"+Name+".jpg",cv.IMREAD_REDUCED_COLOR_2)
            test.append(image)
            self.templates.append(test)

    def find_pos(self, template_name):
        ergebnis = []
        positon = self.template_names.index(template_name)
        template = self.templates[positon]

        name = template[0]
        image = template[1]
        ergebnis.append(name)
        screen = cv.imread("Bilder/screen.jpg",cv.IMREAD_REDUCED_COLOR_2)
        result = cv.matchTemplate(screen, image, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            
        image_w = int(image.shape[1]/2)
        image_h = int(image.shape[0]/2)
        self.log("Best match top left position: %s" % str(max_loc))
        self.log("Best match confidence: %s" %max_val)
        self.log("Found "+name)
        x = (max_loc[0]+image_w)*2
        y = (max_loc[1]+image_h)*2
        werte_pos = []
        werte_pos.append(x)
        werte_pos.append(y)
        ergebnis.append(werte_pos)
        ergebnis.append(max_val)

        return(ergebnis)

