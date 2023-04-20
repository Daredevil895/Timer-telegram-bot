import asyncio

from aiogram import Bot, Dispatcher, executor, types

bot = Bot('6072942376:AAHi9pMtzlrAOD_Byv80FOTyPhETk2iwrGc')
bot_dispatcher = Dispatcher(bot=bot)
channel_id = -1001929429933



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
        await bot.send_message(channel_id, text="Введите кол-во секунд")

    new_message = await bot.send_message(channel_id, text=f"Your timer is at: {timer_seconds}")

    for seconds_left in range(timer_seconds -10, -10, -10):
        await asyncio.sleep(10)
        seconds_left = seconds_left % (24 * 3600) 
        hour = seconds_left // 3600 
        seconds_left %= 3600 
        min = seconds_left // 60 
        seconds_left %= 60

        await new_message.edit_text(f"Your timer is at:{hour}h {min}m {seconds_left}s")


 

if __name__ == '__main__':
    executor.start_polling(bot_dispatcher)