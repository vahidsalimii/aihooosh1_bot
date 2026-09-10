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
            "━━━━━━━━━━━━━━\n"
            "🧠 AI از صفر تا کاربرد\n"
            "🆕 اخبار هوش مصنوعی\n"
            "🛠 ابزارهای جدید AI\n"
            "💡 کاربردهای واقعی AI\n"
            "🎯 مسیر شروع یادگیری\n"
            "━━━━━━━━━━━━━━\n\n"
            "برای ورود به هر بخش، فعلاً دستور مربوط به آن را ارسال کنید.\n\n"
            "مثلاً:\n"
            "🧠 /learn\n"
            "🆕 /news\n"
            "🛠 /tools\n"
            "💡 /usecases\n"
            "🎯 /roadmap"
        )

    elif message.content == "/learn":
        await message.reply(
            "🧠 AI از صفر تا کاربرد\n\n"
            "یک مسیر آموزشی مرحله‌به‌مرحله برای آشنایی "
            "با هوش مصنوعی و استفاده واقعی از آن.\n\n"
            "به‌زودی فصل اول را شروع می‌کنیم."
        )

    elif message.content == "/news":
        await message.reply(
            "🆕 اخبار هوش مصنوعی\n\n"
            "به‌زودی جدیدترین اخبار مهم AI "
            "به زبان ساده در این بخش قرار می‌گیرد."
        )

    elif message.content == "/tools":
        await message.reply(
            "🛠 ابزارهای جدید AI\n\n"
            "ابزارهای جدید و کاربردی هوش مصنوعی "
            "را اینجا معرفی می‌کنیم."
        )

    elif message.content == "/usecases":
        await message.reply(
            "💡 کاربردهای واقعی AI\n\n"
            "اینجا به‌جای معرفی تئوری، "
            "کاربردهای واقعی و قابل اجرا را می‌بینید."
        )

    elif message.content == "/roadmap":
        await message.reply(
            "🎯 مسیر شروع یادگیری AI\n\n"
            "از صفر شروع می‌کنیم و قدم‌به‌قدم "
            "به استفاده حرفه‌ای‌تر از AI می‌رسیم."
        )

    else:
        await message.reply(
            "برای شروع، /start را بزن. 🤖"
        )


bot.run()
