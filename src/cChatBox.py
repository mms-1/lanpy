from src import npyscreen
import configparser


class ChatBox(npyscreen.BoxTitle):
    def create(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        playerConfig = config['Player']
        nick = playerConfig['nick']
        self.name = nick    # TODO Handle config.ini absence errors

    def when_cursor_moved(self):
        self.parent.parentApp.queue_event(
            npyscreen.Event("event_chatbox_change_cursor"))

    def update_messages(self):
        data = ['123', '567']
        self.values = data
        self.entry_widget.start_display_at = 0
        self.entry_widget.cursor_line = 3
        # self.name = "DummyName"
        self.footer = "DummyStatus"
        self.display()
