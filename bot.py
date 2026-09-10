
import os
from bale import Bot, Update, Message

TOKEN = os.getenv("BALE_TOKEN")

bot = Bot(token=TOKEN)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")


@bot.event
async def on_message(message: Message):
    if message.content == "/start":
        await message.reply(
            "سلام 👋\n\n"
            "به بازوی AIHOOOSH خوش آمدید 🤖\n\n"
            "اینجا قراره هوش مصنوعی رو ساده و کاربردی یاد بگیریم."
        )
    else:
        await message.reply(
            "پیامت رو دریافت کردم 🤖\n"
            "به‌زودی قابلیت‌های بیشتری به AIHOOOSH اضافه می‌کنیم."
        )


bot.run()
