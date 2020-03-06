import curses
from src import npyscreen
from src.cUserListBox import UserListBox
from src.cInputBox import InputBox
from src.cChatBox import ChatBox


class MainForm(npyscreen.FormBaseNew):
    def create(self):
        self.add_event_hander("event_user_list_select", self.event_user_list_select)
        self.add_event_hander("event_update_main_form", self.event_update_main_form)
        self.add_event_hander("event_inputbox_send", self.message_send)

        y, x = self.useable_space()
        self.userListBox = self.add(UserListBox, name="Users", value=0, relx=1,
                                    max_width=x // 5, rely=1, max_height=-5)
        self.userListBox.create()
        self.chatBox = self.add(ChatBox, rely=1, relx=(x // 5) + 1, max_height=-5, editable=True,
                                      custom_highlighting=True, highlighting_arr_color_data=[0])
        self.chatBox.create()
        self.inputBox = self.add(InputBox, name="Input",
                                 relx=(x // 5) + 1, rely=-7, height=6)

        new_handlers = {
            # exit
            "^Q": self.exit_func,
            155: self.exit_func,
            curses.ascii.ESC: self.exit_func,
            # send message
            "^S": self.message_send,
            curses.ascii.alt(curses.ascii.NL): self.message_send,
            curses.ascii.alt(curses.KEY_ENTER): self.message_send,
        }
        self.add_handlers(new_handlers)

    def event_user_list_select(self, event):
        self.userListBox.update_user_list()

    def event_messagebox_change_cursor(self, event):
        self.chatBox.update()

    def event_update_main_form(self, event):
        self.display()
        self.userListBox.display()
        self.chatBox.display()
        self.inputBox.display()

    def message_send(self, event):
        message = self.inputBox.value.strip()
        if message != "":
            self.chatBox.update_messages()
            self.inputBox.value = ""
            self.inputBox.footer = message
            self.inputBox.display()

    def exit_func(self, _input):
        exit(0)
