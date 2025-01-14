import asyncio

from PySide6.QtWidgets import QProgressBar
from telethon.errors.rpcerrorlist import (
    ChannelPublicGroupNaError,
    UserCreatorError,
    UserNotParticipantError,
)
from telethon.tl.functions.channels import LeaveChannelRequest

from .base import CustomThread
from .client import GetClient
from .messages import LogMsg


class exitChats(CustomThread):
    def __init__(self, progress: QProgressBar) -> None:
        self.progress = progress

    def run(self):
        super().run()

        async def main():
            client = await GetClient(self)
            dialogs = await client.get_dialogs()
            chat_count = len(dialogs)
            self.progress.setMaximum(chat_count)
            x = 0
            success_exit = 0
            LogMsg(f"Начат выход из чатов в количестве {chat_count}", "i")
            for d in dialogs:
                if not d.is_channel() and d.is_group():
                    try:
                        await client(LeaveChannelRequest(d))
                    except (
                        UserCreatorError,
                        UserNotParticipantError,
                        ChannelPublicGroupNaError,
                    ):
                        continue
                    else:
                        success_exit += 1

                    x += 1
                    self.progress.setValue(x)

            await self.success(
                f"Вы успешно вышли из чатов в количестве {success_exit} шт"
            )

        asyncio.run(main())
