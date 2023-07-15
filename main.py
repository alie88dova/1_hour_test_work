from aiogram.utils import executor
from create_bot import dp
from handlers import client
import asyncio
from handlers.events import schulded
from aiogram.contrib.fsm_storage.memory import MemoryStorage


async def on_startup(_):
    print('Бот онлайн')

client.register_handlers_client(dp)

loop = asyncio.get_event_loop()
loop.create_task(schulded())
loop.create_task()

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
