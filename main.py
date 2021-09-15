
from screen_checker import screen_checker
from freunde_anehmen import freunde_anehmen
from freunde_ordnen import freunde_ordnen
from geschenke_annehmen import geschenke_annehmen
from log_out import log_out
from log_in import log_in
import itertools




class Geschenkebot(object):
    def __init__(self):
        self.screen_checker = screen_checker()
        self.freunde_anehmen = freunde_anehmen()
        self.freunde_ordnen = freunde_ordnen()
        self.geschenke_annehmen = geschenke_annehmen()
        self.logout = log_out()
        self.login = log_in()

        self.password = "test123"
        self.usernames = ["123"]
        
        self.list_cycle = itertools.cycle(self.usernames)
        next(self.list_cycle)
        self.Username = next(self.list_cycle)

        self.run()


    def run(self):
        
        while True:
            #screen checken (Warnung , Informationen, sonstiges)
            self.screen_checker.check_screen()

            #Freundschaftsanfragen annehmen
            self.freunde_anehmen.run()
            
            #Freunde nach Geschenk_ordnen
            self.freunde_ordnen.run()

            #Geschenke annehmen
            self.geschenke_annehmen.run()

            #Items leeren

            #ausloggen
            self.logout.run()

            #einloggen
            self.login.run(self.Username, self.password)
            self.Username = next(self.list_cycle)

Geschenkebot = Geschenkebot()
