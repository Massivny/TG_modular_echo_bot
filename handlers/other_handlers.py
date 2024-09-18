from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU

rout = Router()

@rout.message()
async def proceess_reply(message: Message):
    try: 
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])