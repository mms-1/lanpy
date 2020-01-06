from src import npyscreen
from src.cMainForm import MainForm


class App(npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="SecretApp")
