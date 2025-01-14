import asyncio
from asyncio import sleep

from PySide6.QtWidgets import QLineEdit, QProgressBar, QSpinBox
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelsTooMuchError,
)
from telethon.tl.functions.channels import JoinChannelRequest

from .base import CustomThread
from .client import GetClient


class joinChat(CustomThread):
    def __init__(
        self, links_path: QLineEdit, progress: QProgressBar, sleep_time: QSpinBox
    ):
        super().__init__()
        self.links_path = links_path.text()
        self.progress = progress
        self.sleep_time = int(sleep_time.value())

    def run(self) -> None:
        super().run()

        # debugpy.debug_this_thread()
        async def main():
            client = await GetClient(self)
            with open(self.links_path, "r") as urls:
                chats_arr = urls.readlines()
                self.progress.setMaximum(len(chats_arr))
                self.log_sig.emit(
                    f"Начато присоединение к чатам в количестве {len(chats_arr)} шт",
                    "i",
                )
                x = 0
                for c in chats_arr:
                    x += 1
                    try:
                        entity = client.get_entity(c.split("//")[1])
                    except IndexError:
                        self.log_sig.emit(f"Ссылка {c} неправильного формата", "w")
                        continue

                    try:
                        client(JoinChannelRequest(entity))
                        # надо передавать в joinchannelrequest юзернейм чата. это не точно
                    except ChannelsTooMuchError:
                        await self.error(
                            "Вы присоединились к слишком большому количеству чатов. Попытайтесь позже"
                        )

                    except ChannelPrivateError:
                        self.log_sig.emit(
                            f"Вас забанили в чате или этот чат является приватным {c}",
                            "w",
                        )
                        continue

                    except ChannelInvalidError:
                        self.log_sig.emit(f"Ссылка {c} неправильного формата", "w")
                        continue

                    except Exception as e:
                        self.log_sig.emit(e, "e")
                        continue

                    finally:
                        chats_arr.remove(c)
                        # вроде должно выполняться при любом исключении
                    self.progress.setValue(x)
                    await sleep(self.sleep_time)

                await self.success(
                    f"Успешно присоединились к чатам в количестве {len(chats_arr)} шт"
                )
                client.disconnect()

        asyncio.run(main())
