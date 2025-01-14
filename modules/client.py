import asyncio
from asyncio import sleep
from os import path, remove

import aiohttp
from aiohttp.client_exceptions import ClientConnectionError
from telethon import TelegramClient
from telethon.errors import FloodWaitError, PhoneCodeInvalidError, rpcerrorlist

from .global_vars import Vars
from .messages import ErrorMsg, InputMsg, LogMsg


async def GetClient(calling_thread):
    session_file = "Client.session"

    async def disconnect(client=None):
        if client:
            await client.disconnect()
        remove(session_file)

    if Vars.API_ID and Vars.API_HASH:
        calling_thread.log_sig.emit("=== Начато подключение клиента ===", "i")
        session = aiohttp.ClientSession()
        try:
            calling_thread.log_sig.emit("Проверка соединения", "d")
            await session.get("https://google.com")
        except ClientConnectionError:
            calling_thread.error("Проверьте интернет соединение и попытайтесь ещё раз")
        except Exception as e:
            calling_thread._write_exc()
        else:
            if path.exists(session_file):
                calling_thread.log_sig.emit("Проверка существования файла сессии", "d")
                client = TelegramClient("client", Vars.API_ID, Vars.API_HASH)
                client.start()
                return client
            try:
                client = TelegramClient("client", Vars.API_ID, Vars.API_HASH)
            except Exception as e:
                calling_thread._write_exc()
            else:
                try:
                    connect = asyncio.create_task(client.connect())
                    await connect
                    # тут могут быть ошибки потому что inputmsg вызывается не по сигналу
                    phone_number = InputMsg("Номер телефона")
                    send_code = asyncio.create_task(
                        client.send_code_request(phone_number)
                    )
                    await send_code
                    code = InputMsg("Полученный код")
                    try:
                        int(code)
                    except ValueError:
                        await disconnect(client)
                        calling_thread.error(
                            "Нужно вводить не строку, а число. Повторите попытку"
                        )
                    try:
                        start_without_pass = asyncio.create_task(
                            client.start(phone_number, None, code_callback=lambda: code)
                        )
                        await start_without_pass
                    except ValueError:
                        password = InputMsg("Пароль")
                        try:
                            start_with_pass = asyncio.create_task(
                                client.start(
                                    phone_number, password, code_callback=lambda: code
                                )
                            )
                            await start_with_pass
                        except PhoneCodeInvalidError:
                            await disconnect(client)
                            calling_thread.error(ErrorMsg.PHONE_CODE_INVALID)
                    except PhoneCodeInvalidError:
                        await disconnect(client)
                        calling_thread.error(ErrorMsg.PHONE_CODE_INVALID)

                except RuntimeError:
                    await disconnect(client)
                    calling_thread.quit()

                except rpcerrorlist.FloodWaitError as e:
                    await disconnect(client)
                    calling_thread.error(
                        f"Повторите попытку входа через {e.seconds} секунд"
                    )

                except Exception as e:
                    await disconnect(client)
                    calling_thread._write_exc()
                else:
                    return client

        finally:
            await session.close()
    else:
        calling_thread.error("Вы не ввели данные от аккаунта")


# нужно рефакторить эту функцию, так как сообщения об ошибках внутри потока можно давать только по сигналам
async def send_message(client: TelegramClient, dialog, message):
    def get_dialog_info(dialog):
        if dialog.entity.username:
            return f"@{dialog.entity.username}"
        else:
            return dialog.title

    try:
        await client.send_message(dialog, message)
    except rpcerrorlist.ChatWriteForbiddenError:
        LogMsg(f"Вы не можете писать в чат {get_dialog_info()}", "w")

    except FloodWaitError as e:
        sec = e.seconds
        LogMsg(f"Приостановлен спам на {sec} секунд", "w")
        await sleep(sec)
        await client.send_message(dialog, message)

    except Exception as e:
        ErrorMsg(ErrorMsg.UNKOWN_ERROR, e)
        Vars.enable_btn()
