import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
logging.basicConfig(level=logging.INFO)

# Создание объекта бота
bot = Bot(token='7438789045:AAHOrtnYTttADfOAYsT6mPC0i0pV0WfHRJc')

# Создание диспетчера без передачи бота
dp = Dispatcher()

# Хэндлер для команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Создаем инлайн-клавиатуру с кнопкой
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="Открыть Mini App", 
            web_app=types.WebAppInfo(url="https://finory.onrender.com/")
        )
    )
    
    await message.answer(
        "Привет! Нажми кнопку ниже, чтобы открыть Mini App:",
        reply_markup=builder.as_markup()
    )

async def on_startup():
    print('Бот вышел в онлайн')
    await bot.send_message(1030874842, 'Online')


async def main():
    # Привязка объекта бота к диспетчеру
    dp["bot"] = bot
    await on_startup()
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())

