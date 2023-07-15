import asyncio
import hashlib
import sqlite3
from keyboards.client_kb import kb_blocks_end
from create_bot import bot
from handlers.google_sheets import get_sheet
from to_work import list_Tasks, tel_id
import threading


class Task():

    ended = False

    def __init__(self, task: dict):
        self.tel_id = task["tel_id"]
        self.test_text = task["test_text"]
        self.date = task["date"]
        self.time = task["time"]
        self.time_to_do = task["time_to_do"]
        #c помощью индетификатора отправляет готовность задачи
        self.idintificatore = str(hashlib.sha512(
            str(task["tel_id"])+str(task["test_text"])
        ))

    def end_timer(self):
        if self.ended == False:
            await bot.send_message(tel_id, f"{self.tel_id}")

    def start_message(self):
        await bot.send_message(self.tel_id, f"Ваша зачдача {self.test_text}\n"
                                            f"время старта {self.date} {self.time}"
                                            f"окончание через {self.time_to_do}!",
                               reply_markup= await kb_blocks_end(self.idintificatore))


async def schulded():
    while True:
        tasks = get_sheet()
        for task in tasks:
            list_Tasks.append(Task(task))

        await asyncio.sleep(60)


async def start_work():
    while True:
        for task in list_Tasks:
            delay = task.time_to_do
            timer = threading.Timer(delay, task.end_timer)
            timer.start()
        await asyncio.sleep(60)