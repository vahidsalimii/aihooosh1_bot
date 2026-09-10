import os
from bale import (
    Bot,
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

TOKEN = os.getenv("BALE_TOKEN")

bot = Bot(token=TOKEN)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")


@bot.event
async def on_message(message: Message):

    if message.content == "/start":

        keyboard = InlineKeyboardMarkup()

        keyboard.add(
            InlineKeyboardButton(
                text="🧠 AI از صفر تا کاربرد",
                callback_data="learn"
            )
        )

        keyboard.add(
            InlineKeyboardButton(
                text="🆕 اخبار هوش مصنوعی",
                callback_data="news"
            )
        )

        keyboard.add(
            InlineKeyboardButton(
                text="🛠 ابزارهای جدید AI",
                callback_data="tools"
            )
        )

        keyboard.add(
            InlineKeyboardButton(
                text="💡 کاربردهای واقعی AI",
                callback_data="usecases"
            )
        )

        keyboard.add(
            InlineKeyboardButton(
                text="🎯 مسیر یادگیری",
                callback_data="roadmap"
            )
        )

        await message.reply(
            "🤖 AIHOOOSH\n\n"
            "دنیای هوش مصنوعی، ساده و کاربردی.\n\n"
            "یک بخش را انتخاب کن:",
            components=keyboard
        )


@bot.event
async def on_callback(callback: CallbackQuery):

    if callback.data == "learn":
        await callback.message.reply(
            "🧠 AI از صفر تا کاربرد\n\n"
            "مسیر آموزشی مرحله‌به‌مرحله AIHOOOSH\n"
            "از آشنایی با هوش مصنوعی تا استفاده حرفه‌ای."
        )

    elif callback.data == "news":
        await callback.message.reply(
            "🆕 اخبار هوش مصنوعی\n\n"
            "به‌زودی جدیدترین اخبار مهم AI "
            "به زبان ساده در این بخش قرار می‌گیرد."
        )

    elif callback.data == "tools":
        await callback.message.reply(
            "🛠 ابزارهای جدید AI\n\n"
            "ابزارهای جدید و کاربردی هوش مصنوعی "
            "را اینجا معرفی می‌کنیم."
        )

    elif callback.data == "usecases":
        await callback.message.reply(
            "💡 کاربردهای واقعی AI\n\n"
            "اینجا کاربردهای واقعی و قابل اجرا "
            "هوش مصنوعی را می‌بینید."
        )

    elif callback.data == "roadmap":
        await callback.message.reply(
            "🎯 مسیر یادگیری AI\n\n"
            "از صفر شروع می‌کنیم و قدم‌به‌قدم "
            "به استفاده حرفه‌ای‌تر از AI می‌رسیم."
        )


bot.run()
