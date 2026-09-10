import os
from bale import Bot, Message, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BALE_TOKEN")

bot = Bot(token=TOKEN)


def main_menu():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🧠 AI از صفر تا کاربرد",
                    callback_data="learn"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🆕 اخبار AI",
                    callback_data="news"
                ),
                InlineKeyboardButton(
                    text="🛠 ابزارهای جدید",
                    callback_data="tools"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💡 کاربردهای واقعی AI",
                    callback_data="usecases"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎯 از کجا شروع کنم؟",
                    callback_data="start_ai"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ℹ️ درباره AIHOOOSH",
                    callback_data="about"
                )
            ]
        ]
    )


@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")


@bot.event
async def on_message(message: Message):

    if message.content == "/start":
        await message.reply(
            "🤖 AIHOOOSH\n\n"
            "دنیای هوش مصنوعی، ساده و کاربردی.\n\n"
            "اینجا می‌تونی AI رو یاد بگیری، "
            "ابزارهای جدید رو بشناسی و کاربردهای واقعی "
            "هوش مصنوعی رو ببینی.\n\n"
            "از کجا شروع کنیم؟ 👇",
            components=main_menu()
        )

    else:
        await message.reply(
            "برای استفاده از امکانات AIHOOOSH، "
            "دستور /start را بزن. 🤖"
        )


bot.run()
