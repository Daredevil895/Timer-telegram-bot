import os
import asyncio
from aiogram import Bot, Dispatcher, executor, types

from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
bot_dispatcher = Dispatcher(bot=bot)
channel_id = os.getenv('kanal')



@bot_dispatcher.message_handler(commands=["stop"])
async def command_stop(message: types.Message):
    #тут код, который останавливает цикл While True из функции "start_parsing"
    await bot.send_message(channel_id, text="Бот остановлен")
    new_timer_massage = False

@bot_dispatcher.message_handler()
async def new_timer_massage(message):
    try:
        timer_seconds = int(message.text)
        if timer_seconds <= 0:
            raise ValueError()
        
    except (TypeError, ValueError):
        await bot.send_message(channel_id, text="---Введите кол-во секунд---")

    new_message = await bot.send_message(channel_id, text=f"-+-Твой таймер на: {timer_seconds}s-+-")

    for seconds_left in range(timer_seconds -10, -10, -10):
        await asyncio.sleep(10)

        if seconds_left < 10:
            await new_message.edit_text(f"---Твой таймер стоит на---\n---{hour}:{min}:{seconds_left}---")
            await asyncio.sleep(seconds_left)
            seconds_left = seconds_left - seconds_left

        seconds_left = seconds_left % (24 * 3600) 
        hour = seconds_left // 3600 
        seconds_left %= 3600 
        min = seconds_left // 60 
        seconds_left %= 60

        await new_message.edit_text(f"---Твой таймер стоит на---\n---{hour}:{min}:{seconds_left}---")
        



if __name__ == '__main__':
    executor.start_polling(bot_dispatcher)