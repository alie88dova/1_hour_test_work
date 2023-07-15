import types

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage #Переделать на рэдис можно позже\

storage = MemoryStorage()

bot = Bot(token="TOKEN")
#Start dispatcher to use handlers and our storage
dp = Dispatcher(bot, storage=storage)

