import datetime
import sqlite3
from create_bot import bot
from aiogram import types, Dispatcher
from aiogram.types import ContentType
from to_work import list_Tasks, tel_id
from handlers.events import Task

async def pick_do(call: types.CallbackQuery):
    for task in list_Tasks:
        if task.idintificatore == call.data.split()[1]:
            task.ended = True
            await bot.send_message(tel_id, f"{task.tel_id} завершил задача {task.test_text}")


async def pick_not_do(call: types.CallbackQuery):
    for task in list_Tasks:
        if task.idintificatore == call.data.split()[1]:
            task.ended = True
            await bot.send_message(tel_id, f"{task.tel_id} не завершил задача {task.test_text}")


def register_handlers_client(dp: Dispatcher):

    dp.register_callback_query_handler(pick_do, lambda x: x.data and x.data.startswith('task_do '))
    dp.register_callback_query_handler(pick_not_do, lambda x: x.data and x.data.startswith('task_not_do '))

