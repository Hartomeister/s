from aiogram import Bot, Dispatcher, executor, types
from configure import telegram_token, shark_stiker
import logging
import asyncio
import nekos

logging.basicConfig(level=logging.INFO)

bot = Bot(token=telegram_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_handler(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1)
    btns_text = ('Neko', 'Holo', 'Fox girl')
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
    btns_text = ('Ngif (Gif)', 'Pat (Gif)', 'Hug (Gif)')
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
    await message.answer("\nПривет, я тебе могу помочь найти аниме тянку🥵😏 \nПоддержка: @BooleanFox",
                         reply_markup=keyboard_markup, parse_mode='html')
    await message.answer_sticker(sticker=shark_stiker)


@dp.message_handler()
async def all_msg_handler(message: types.Message):
    if message.text == 'Neko':
        await message.answer_photo(nekos.img('neko'))
    if message.text == 'Holo':
        await message.answer_photo(nekos.img('holo'))
    if message.text == 'Fox girl':
        await message.answer_photo(nekos.img('fox_girl'))
    if message.text == 'Ngif (Gif)':
        await message.answer_video(nekos.img('ngif'))
    if message.text == 'Hug (Gif)':
        await message.answer_video(nekos.img('hug'))
    if message.text == 'Pat (Gif)':
        await message.answer_video(nekos.img('pat'))


if __name__ == '__main__':
    executor.start_polling(dp)
