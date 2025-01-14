import logging

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QInputDialog, QLineEdit, QMessageBox

from modules.global_vars import Vars

logging.basicConfig(
    filename="log.txt",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s:%(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)


class Base(QMessageBox):
    def __init__(self, msg, level, action="Выполнение продолжено") -> None:
        super().__init__(parent=None)
        LogMsg(msg, level)
        eval(f"LogMsg(LogMsg.{action}, '{level}')")


class ErrorMsg(Base, QObject):
    UNKOWN_ERROR = "Неизвестная ошибка"
    PHONE_CODE_INVALID = "Вы ввели неверный код. Повторите попытку"
    NO_DESCRIPTION = "Нет полного описания"

    @Slot(str, str)
    def __init__(self, text, dt=NO_DESCRIPTION) -> None:
        if text == self.UNKOWN_ERROR:
            super().__init__(str(dt), "c", "ACTION_CANCELED")
        else:
            super().__init__(text, "e", "ACTION_CANCELED")
        self.setWindowTitle("Ошибка")
        self.setIcon(self.Icon.Critical)
        self.setStandardButtons(self.StandardButton.Ok)
        self.setInformativeText("Полный текст об ошибке")
        self.setText(text)
        if dt == "":
            self.setDetailedText(self.NO_DESCRIPTION)
        else:
            self.setDetailedText(str(dt))
        self.exec()
        if bool(self.clickedButton().text()):
            Vars.terminate_sig.emit()


class WarnMsg(Base):
    @Slot(str)
    def __init__(self, text) -> None:
        super().__init__(text, "w")
        # self.warnMessage = QMessageBox()
        self.warning("Предупреждение", text, QMessageBox, parent=None)
        # self.warnMessage.setWindowTitle('Предупреждение')
        # self.warnMessage.setIcon(QMessageBox.Warning)
        # self.warnMessage.setStandardButtons(QMessageBox.Ok)
        # self.warnMessage.setInformativeText('Полный текст об ошибке')
        # self.warnMessage.setText(text)
        # self.warnMessage.setDetailedText(self.detailed)
        self.exec()


class LogMsg:
    ACTION_CANCELED = "--- Действие прервано ---"
    ACTION_COMPLETED = "+++ Действие завершено +++"
    OPEN_FOLDER = "Открытие диалога выбора папки"
    levels = {"i": "info", "w": "warning", "e": "error", "c": "critical", "d": "debug"}

    @Slot(str, str)
    def __init__(self, msg, level) -> None:
        Vars.log.append(msg)
        eval(f"logging.{self.levels[level]}('{msg}')")


class OkMsg(Base):
    @Slot(str)
    def __init__(self, text) -> None:
        super().__init__(text, "i", "ACTION_COMPLETED")
        # self.okMessage = QMessageBox()
        self.information("Успех", text, QMessageBox.StandardButton.Ok, parent=None)
        # self.okayMessage.setWindowTitle('Успех')
        # self.okayMessage.setStandardButtons(QMessageBox.Ok)
        # self.okayMessage.setIcon(QMessageBox.Information)
        # self.okayMessage.setText(text)
        self.exec()


class InputMsg(QObject):
    interrupt_sig = Signal(int)

    @Slot(str)
    def show(self, msg) -> None:
        self.text, self.ok = QInputDialog().getText(
            None, "Ввод", msg, QLineEdit.EchoMode.Normal
        )
        if not self.text and self.ok:
            ErrorMsg("Вы не ввели данные. Повторите попытку")
        elif not self.ok:
            # pass # здесь нужно прервать выполнение потока
            self.interrupt_sig.emit()

        elif self.text and self.ok:
            return self.text


# def InputMsg(message):
#     text, ok = QInputDialog().getText(None, 'Ввод',
#                                       message, QLineEdit.Normal)

#     if not text and ok:
#         ErrorMsg('Вы не ввели данные. Повторите попытку')
#         raise RuntimeError

#     elif not ok:
#         raise RuntimeError

#     elif text and ok:
#         return text
