import traceback

from PySide6.QtCore import QThread, Signal

from .global_vars import Vars
from .messages import ErrorMsg, InputMsg, LogMsg, OkMsg, WarnMsg


class CustomThread(QThread, Vars):
    error_sig = Signal(str, str)
    log_sig = Signal(str, str)
    warn_sig = Signal()
    ok_sig = Signal(str)
    finished = Signal()
    input_sig = Signal()
    terminate_sig = Signal()

    def __init__(self):
        super().__init__(parent=None)
        self.error_sig.connect(ErrorMsg)
        self.warn_sig.connect(WarnMsg)
        self.log_sig.connect(LogMsg)
        self.ok_sig.connect(OkMsg)
        self.input_sig.connect(InputMsg)
        # self.mutex = QMutex()
        # btn_ok_sig = ErrorMsg.buttonClicked
        # btn_ok_sig.connect(self.exec_)
        # self.terminate_sig.connect(self.terminate_thread)
        # InputMsg.interrupt_sig.connect(self.exec_)
        self.setTerminationEnabled(True)

    def run(self):
        if hasattr(self, "progress"):
            eval("self.progress.setValue(0)")

    def _write_exc(self):
        exc = traceback.format_exc()
        self.error_sig.emit(ErrorMsg.UNKOWN_ERROR, exc)

    def error(self, text, dt="Нет полного описания"):
        self.error_sig.emit(text, dt)
        raise RuntimeError
        # self.exec_()

    def success(self, text):
        self.ok_sig.emit(text)
        self.exec_()

    @Signal
    def exec_(self) -> int:
        self.finished.emit()
        return super().exec()
