from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

async def kb_blocks_end(idintificatore: str) -> InlineKeyboardMarkup:

    kb_section = InlineKeyboardMarkup()
    button_end = InlineKeyboardButton(f'Выполено', callback_data=f'task_do {idintificatore}')
    button_reject = InlineKeyboardButton(f'Не сделано', callback_data=f'task_not_do {idintificatore}')
    kb_section.row(button_end)
    kb_section.row(button_reject)

    return kb_section