import os
from bale import Bot, Message

TOKEN = os.getenv("BALE_TOKEN")

bot = Bot(token=TOKEN)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")


@bot.event
async def on_message(message: Message):

    if message.content == "/start":
        await message.reply(
            "🤖 AIHOOOSH\n\n"
            "دنیای هوش مصنوعی، ساده و کاربردی.\n\n"
            "🧠 AI از صفر تا کاربرد\n"
            "🆕 اخبار هوش مصنوعی\n"
            "🛠 ابزارهای جدید AI\n"
            "💡 کاربردهای واقعی AI\n"
            "🎯 مسیر شروع یادگیری\n\n"
            "به‌زودی این بخش‌ها را به منوی تعاملی تبدیل می‌کنیم."
        )

    else:
        await message.reply(
            "برای شروع، /start را بزن. 🤖"
        )


bot.run()
