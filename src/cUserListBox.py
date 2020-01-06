from src import npyscreen


class UserListBox(npyscreen.BoxTitle):
    def create(self):
        pass

    def when_value_edited(self):
        # event to change message dialog box
        self.parent.parentApp.queue_event(
            npyscreen.Event("event_user_list_select"))

    def update_user_list(self):
        # TODO pull data from server
        data = ['hello', 'world', '!']

        self.values = data

        # this event update all boxes
        self.parent.parentApp.queue_event(
            npyscreen.Event("event_update_main_form"))
