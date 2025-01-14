from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

from modules.chat_spam import ChatSpam
from modules.exit import exitChats
from modules.global_vars import Vars
from modules.join import joinChat
from modules.messages import ErrorMsg, LogMsg
from ui import Ui_MainWindow


class ConnectButtons(Ui_MainWindow, QMainWindow):
    terminate_sig = Signal()

    def __init__(self, parent=None):
        super(ConnectButtons, self).__init__(parent=parent)
        self.setupUi(self)
        self.terminate_sig.connect(self.terminate_thread)
        self.__sender = None
        # self.__thread = None

        Vars.log = self.log
        Vars.enable_btn = self.enable_btn
        Vars.disable_btn = self.disable_btn
        Vars.terminate_sig = self.terminate_sig

        self.lne_api_hash.textChanged.connect(self.update_api_hash)
        self.lne_api_id.setValidator(QIntValidator(0, 99999999, parent=self))
        self.lne_api_id.textChanged.connect(self.update_api_id)

        self.btn_chat_action.clicked.connect(self.chat_actions)
        self.btn_chat_spam.clicked.connect(self.chat_spam)
        self.btn_private_spam.clicked.connect(self.private_chats_spam)
        self.btn_start_invite.clicked.connect(self.start_invite)
        self.btn_start_dump.clicked.connect(self.start_dump)
        self.btn_open_links.clicked.connect(self.open_links_file)

        self.rd_join_chat.clicked.connect(self.enable_join_chat)
        self.rd_exit_from_chats.clicked.connect(self.disable_join_chat)

        self.rd_list_spam.clicked.connect(self.enable_list_spam)
        self.rd_db_spam.clicked.connect(self.disable_list_spam)

        self.rd_list_invite.clicked.connect(self.enable_list_invite)
        self.rd_db_invite.clicked.connect(self.disable_list_invite)

    def chat_spam(self):
        message_text = self.t_edit_message.toPlainText()
        if message_text == "":
            ErrorMsg("Вы не ввели текст сообщения")
        elif len(message_text) >= 4096:
            ErrorMsg("Сообщение слишком длинное")
        self.__sender = self.sender()
        self.disable_btn()
        self.thread_spam = ChatSpam(
            self.chat_spam_progress,
            self.sb_chat_spam_repeats,
            self.t_edit_message,
            self.sb_message_delay,
        )
        self.thread_spam.finished.connect(self.enable_btn)
        self.thread_spam.start()

    def chat_actions(self):
        if self.rd_join_chat.isChecked():
            if self.lne_chat_links.text() != "":
                self.__sender = self.sender()
                # self.__thread = "self.thread_join"
                self.disable_btn()
                self.thread_join = joinChat(
                    self.lne_chat_links, self.chat_action_progress, self.sb_join_delay
                )
                # self.thread_join.finished.connect(self.terminate_thread)
                self.thread_join.start()
                self.thread_join.terminate()
            else:
                ErrorMsg("Вы не выбрали файл с ссылками на каналы")

        elif self.rd_exit_from_chats.isChecked():
            self.disable_btn()
            self.thread_exit = exitChats(self.chat_action_progress)
            self.thread_exit.finished.connect(self.enable_btn)
            self.thread_exit.start()

    def private_chats_spam(self):
        message_text = self.t_edit_message.toPlainText()
        if message_text == "":
            ErrorMsg("Вы не ввели текст сообщения")
        elif len(message_text) >= 4096:
            ErrorMsg("Сообщение слишком длинное")

        if self.rd_db_spam.isChecked():
            pass
        elif self.rd_list_spam.isChecked():
            pass

    def start_invite(self):
        if self.rd_db_invite.isChecked():
            pass
        elif self.rd_list_invite.isChecked():
            pass

    def save_log(self):
        pass

    def start_dump(self):
        pass

    def open_links_file(self):
        self.open_file("Выберите файл с ссылками на каналы", "lne_chat_links")

    def open_file(self, text, line_edit):
        self.log.appendPlainText(LogMsg.OPEN_FOLDER)
        file_path = QFileDialog.getOpenFileName(None, text, ".")[0]
        eval(f"self.{line_edit}.setText('{file_path}')")

    def update_api_id(self):
        Vars.API_ID = self.lne_api_id.text()

    def update_api_hash(self):
        Vars.API_HASH = self.lne_api_hash.text()

    def enable_join_chat(self):
        self.set_status(
            "enable",
            "label",
            "lne_chat_links",
            "btn_open_links",
            "label_2",
            "sb_join_delay",
        )

    def disable_join_chat(self):
        self.set_status(
            "disable",
            "label",
            "lne_chat_links",
            "btn_open_links",
            "label_2",
            "sb_join_delay",
        )

    def enable_list_spam(self):
        self.set_status("enable", "label_7", "lne_phones_path", "btn_open_phones")

    def disable_list_spam(self):
        self.set_status("disable", "label_7", "lne_phones_path", "btn_open_phones")

    def enable_list_invite(self):
        self.set_status(
            "enable",
            "label_10",
            "lne_phones_path_2",
            "lne_phones_path_2",
            "btn_open_phones_2",
        )

    def disable_list_invite(self):
        self.set_status(
            "disable",
            "label_10",
            "lne_phones_path_2",
            "lne_phones_path_2",
            "btn_open_phones_2",
        )

    def enable_chat_spam(self):
        self.set_status("enable", "sb_chat_spam_repeats")

    def disable_chat_spam(self):
        self.set_status("disable", "sb_chat_spam_repeats")

    def set_status(self, status, *args):
        for i in args:
            if status == "enable":
                eval(f"self.{i}.setEnabled(True)")
            elif status == "disable":
                eval(f"self.{i}.setDisabled(True)")

    @Slot()
    def disable_btn(self):
        self.__sender.setDisabled(True)

    @Slot()
    def enable_btn(self):
        self.__sender.setEnabled(True)

    @Slot()
    def terminate_thread(self):
        # eval(f"{thread}.terminate()")
        self.thread_join.terminate()
        self.enable_btn()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    c = ConnectButtons()
    c.show()
    sys.exit(app.exec())
