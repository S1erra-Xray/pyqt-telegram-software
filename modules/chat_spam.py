import asyncio
from asyncio import sleep

from PySide6.QtWidgets import QProgressBar, QSpinBox, QTextEdit

from .base import CustomThread
from .client import GetClient, send_message
from .messages import LogMsg


class ChatSpam(CustomThread):
    def __init__(
        self,
        progress: QProgressBar,
        repeats: QSpinBox,
        message: QTextEdit,
        sleep_time: QSpinBox,
    ):
        super().__init__()
        self.progress = progress
        self.repeats = repeats.value()
        self.message = message.toPlainText()
        self.sleep_time = int(sleep_time.value())

    def run(self):
        super().run()

        async def main():
            client = await GetClient(self)
            LogMsg(
                f"Начат спам по чатам с повторами в количестве шт {self.repeats}", "i"
            )
            for r in range(self.repeats):
                async for d in await client.iter_dialogs():
                    if not d.is_channel() and d.is_group():
                        await send_message(client, d, self.message)

                LogMsg(f"Выполнен {r} по счёту повтор", "i")
                await sleep(self.sleep_time)

            await self.success(
                f"Спам закончен. Было выполнено повторов в количестве {self.repeats} шт"
            )
            client.disconnect()

        asyncio.run(main())
