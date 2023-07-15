from aiogram.utils import executor
from create_bot import dp
from handlers import client
import asyncio
from handlers.events import append_to_list, start_work


async def on_startup(_):
    print('Бот онлайн')

client.register_handlers_client(dp)

loop = asyncio.get_event_loop()
loop.create_task(append_to_list())
loop.create_task(start_work())

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
