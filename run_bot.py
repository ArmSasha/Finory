import logging
from aiogram import Bot, Dispatcher
import asyncio

logging.basicConfig(level=logging.INFO)

# Создание объекта бота
bot = Bot(token='7438789045:AAHOrtnYTttADfOAYsT6mPC0i0pV0WfHRJc')

# Создание диспетчера без передачи бота
dp = Dispatcher()


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

