#!/usr/bin/env python3
import npyscreen


class App(npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Hello Habr!")


class MainForm(npyscreen.ActionForm):
    # Конструктор
    def create(self):
        y, x = self.useable_space()
        self.title = self.add(npyscreen.TitleText,
                              name="TitleText",
                              value="Hello World!")
        self.add(npyscreen.TitleDateCombo, name="Date:", max_width=x // 2)
        self.add(npyscreen.TitleMultiSelect, relx=x // 2 + 1, rely=2,
                 value=[1, 2],
                 name="Pick Several",
                 values=["Option1", "Option2", "Option3"],
                 scroll_exit=True)

    # переопределенный метод, срабатывающий при нажатии на кнопку «ok»
    def on_ok(self):
        self.parentApp.setNextForm(None)

    # переопределенный метод, срабатывающий при нажатии на кнопку «cancel»
    def on_cancel(self):
        self.title.value = "Hello World!"


MyApp = App()
MyApp.run()
