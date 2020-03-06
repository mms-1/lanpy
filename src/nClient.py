from src import npyscreen
from src.cLanClient import LanClient
from src.cMainForm import MainForm


class App(npyscreen.StandardApp):
    NICK = "NoName"

    def onStart(self):
        self.addForm("MAIN", MainForm, name="SecretApp")
