from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from lexicon.lexicon import LEXICON_RU

rout = Router()

@rout.message(Command('start'))
async def process_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'])

@rout.message(Command('help'))
async def process_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'])