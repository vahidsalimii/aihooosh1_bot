import os

from bale import (
    Bot,
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from news import format_news
from tools import format_category


TOKEN = os.getenv("BALE_TOKEN")

bot = Bot(token=TOKEN)


# ==================================================
# MAIN MENU
# ==================================================

def main_menu():

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

    return keyboard


# ==================================================
# TOOLS MENU
# ==================================================

def tools_menu():

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text="✍️ متن و تولید محتوا",
            callback_data="tool_text"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🎨 تصویر و طراحی",
            callback_data="tool_image"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🎬 ویدئو",
            callback_data="tool_video"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🎙 صدا",
            callback_data="tool_voice"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🔎 تحقیق و جستجو",
            callback_data="tool_research"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="⚡ بهره‌وری و کار",
            callback_data="tool_productivity"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🔙 منوی اصلی",
            callback_data="main"
        )
    )

    return keyboard


# ==================================================
# TOOL BACK MENU
# ==================================================

def tool_back_menu():

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text="🛠 بازگشت به بانک ابزارها",
            callback_data="tools"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🏠 منوی اصلی",
            callback_data="main"
        )
    )

    return keyboard


# ==================================================
# LEARNING MENU
# ==================================================

def learning_menu():

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text="📘 فصل ۱ — آشنایی با AI",
            callback_data="chapter1"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🧩 فصل ۲ — کار کردن با AI",
            callback_data="chapter2"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🚀 فصل ۳ — استفاده واقعی",
            callback_data="chapter3"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🎯 فصل ۴ — حرفه‌ای‌تر شدن",
            callback_data="chapter4"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🔙 منوی اصلی",
            callback_data="main"
        )
    )

    return keyboard


# ==================================================
# CHAPTER 1
# ==================================================

def chapter1_menu():

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text="1️⃣ هوش مصنوعی چیست؟",
            callback_data="lesson1"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="2️⃣ AI چگونه کار می‌کند؟",
            callback_data="lesson2"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="3️⃣ مدل‌های هوش مصنوعی",
            callback_data="lesson3"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="4️⃣ تفاوت AI و ابزارهای AI",
            callback_data="lesson4"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="5️⃣ از کجا شروع کنیم؟",
            callback_data="lesson5"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🔙 بازگشت",
            callback_data="learn"
        )
    )

    return keyboard


# ==================================================
# CHAPTER 2
# ==================================================

def chapter2_menu():

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text="6️⃣ چگونه با AI صحبت کنیم؟",
            callback_data="lesson6"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="7️⃣ پرامپت چیست؟",
            callback_data="lesson7"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="8️⃣ ساخت پرامپت بهتر",
            callback_data="lesson8"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="9️⃣ خطاهای رایج",
            callback_data="lesson9"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🔟 گرفتن نتیجه بهتر",
            callback_data="lesson10"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🔙 بازگشت",
            callback_data="learn"
        )
    )

    return keyboard


# ==================================================
# CHAPTER 3
# ==================================================

def chapter3_menu():

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text="1️⃣1️⃣ AI در تولید محتوا",
            callback_data="lesson11"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="1️⃣2️⃣ AI در کسب‌وکار",
            callback_data="lesson12"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="1️⃣3️⃣ AI برای تحقیق",
            callback_data="lesson13"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="1️⃣4️⃣ AI برای تصویر",
            callback_data="lesson14"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="1️⃣5️⃣ AI برای ویدئو و صدا",
            callback_data="lesson15"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🔙 بازگشت",
            callback_data="learn"
        )
    )

    return keyboard


# ==================================================
# CHAPTER 4
# ==================================================

def chapter4_menu():

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text="1️⃣6️⃣ ساخت سیستم کاری با AI",
            callback_data="lesson16"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="1️⃣7️⃣ ترکیب چند ابزار AI",
            callback_data="lesson17"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="1️⃣8️⃣ اتوماسیون با AI",
            callback_data="lesson18"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="1️⃣9️⃣ ساخت دستیار شخصی",
            callback_data="lesson19"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="2️⃣0️⃣ تبدیل AI به مهارت واقعی",
            callback_data="lesson20"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🔙 بازگشت",
            callback_data="learn"
        )
    )

    return keyboard


# ==================================================
# LESSONS
# ==================================================

lessons = {

    "lesson1":
        "1️⃣ هوش مصنوعی چیست؟\n\n"
        "AI مجموعه‌ای از فناوری‌هاست که به کامپیوتر "
        "اجازه می‌دهد بعضی کارهایی را انجام دهد که "
        "معمولاً به توانایی انسانی نیاز دارند.\n\n"
        "مثلاً فهمیدن متن، تولید تصویر، تحلیل اطلاعات "
        "و پاسخ دادن به سؤال‌ها.",

    "lesson2":
        "2️⃣ AI چگونه کار می‌کند؟\n\n"
        "مدل‌های AI با استفاده از داده‌های زیاد، "
        "الگوها را یاد می‌گیرند و سپس بر اساس "
        "ورودی ما خروجی تولید می‌کنند.\n\n"
        "داده → یادگیری → درخواست → پاسخ",

    "lesson3":
        "3️⃣ مدل‌های هوش مصنوعی\n\n"
        "مدل‌های مختلف برای کارهای مختلف ساخته شده‌اند.\n\n"
        "📝 متن\n"
        "🖼 تصویر\n"
        "🎬 ویدئو\n"
        "🎙 صدا\n"
        "📊 تحلیل داده",

    "lesson4":
        "4️⃣ تفاوت AI و ابزارهای AI\n\n"
        "AI فناوری است.\n"
        "ابزار AI محصولی است که این فناوری را "
        "برای انجام یک کار در اختیار ما قرار می‌دهد.",

    "lesson5":
        "5️⃣ از کجا شروع کنیم؟\n\n"
        "1. شناخت AI\n"
        "2. یادگیری پرامپت\n"
        "3. شناخت ابزارها\n"
        "4. حل مسائل واقعی\n"
        "5. ساخت سیستم کاری",

    "lesson6":
        "6️⃣ چگونه با AI صحبت کنیم؟\n\n"
        "AI ذهن‌خوان نیست.\n"
        "هرچه درخواست ما واضح‌تر باشد، احتمال "
        "گرفتن نتیجه بهتر بیشتر می‌شود.",

    "lesson7":
        "7️⃣ پرامپت چیست؟\n\n"
        "Prompt همان دستوری است که به AI می‌دهیم.\n\n"
        "یک پرامپت خوب می‌تواند شامل:\n"
        "هدف + اطلاعات + محدودیت + خروجی موردنظر باشد.",

    "lesson8":
        "8️⃣ ساخت پرامپت بهتر\n\n"
        "یک ساختار ساده:\n\n"
        "نقش + هدف + اطلاعات + محدودیت + خروجی",

    "lesson9":
        "9️⃣ خطاهای رایج\n\n"
        "❌ درخواست مبهم\n"
        "❌ اطلاعات ناکافی\n"
        "❌ قبول کردن اولین پاسخ\n"
        "❌ مشخص نکردن خروجی",

    "lesson10":
        "🔟 گرفتن نتیجه بهتر\n\n"
        "اگر نتیجه خوب نبود، ابتدا درخواست را اصلاح کن.\n"
        "اطلاعات بیشتری بده و فرمت خروجی را مشخص کن.",

    "lesson11":
        "1️⃣1️⃣ AI در تولید محتوا\n\n"
        "ایده‌پردازی، تحقیق، نوشتن، تصویر، ویدئو "
        "و بسیاری از مراحل تولید محتوا را می‌توان "
        "با AI سریع‌تر کرد.",

    "lesson12":
        "1️⃣2️⃣ AI در کسب‌وکار\n\n"
        "تحقیق بازار، تولید محتوا، تحلیل اطلاعات، "
        "ارتباط با مشتری و بهینه‌سازی فرآیندها "
        "از کاربردهای مهم AI هستند.",

    "lesson13":
        "1️⃣3️⃣ AI برای تحقیق\n\n"
        "AI می‌تواند در جمع‌آوری، دسته‌بندی، "
        "مقایسه و خلاصه‌سازی اطلاعات کمک کند.\n\n"
        "اطلاعات مهم را همیشه با منابع معتبر بررسی کن.",

    "lesson14":
        "1️⃣4️⃣ AI برای تصویر\n\n"
        "با AI می‌توان ایده‌های تصویری را به تصویر تبدیل کرد.\n\n"
        "توصیف موضوع، سبک، نور، محیط و ترکیب‌بندی "
        "به نتیجه بهتر کمک می‌کند.",

    "lesson15":
        "1️⃣5️⃣ AI برای ویدئو و صدا\n\n"
        "AI می‌تواند در سناریو، تصویر، صداگذاری، "
        "تدوین و تولید ویدئو کمک کند.",

    "lesson16":
        "1️⃣6️⃣ ساخت سیستم کاری با AI\n\n"
        "استفاده حرفه‌ای یعنی AI را وارد فرآیند کاری کنیم.\n\n"
        "ورودی → تحلیل → تولید → بررسی → اصلاح → خروجی",

    "lesson17":
        "1️⃣7️⃣ ترکیب چند ابزار AI\n\n"
        "گاهی بهترین نتیجه با ترکیب چند ابزار به دست می‌آید.\n\n"
        "هر ابزار می‌تواند یک بخش مشخص از فرآیند را انجام دهد.",

    "lesson18":
        "1️⃣8️⃣ اتوماسیون با AI\n\n"
        "اتوماسیون یعنی بعضی کارهای تکراری را "
        "با دخالت کمتر انسان انجام دهیم.",

    "lesson19":
        "1️⃣9️⃣ ساخت دستیار شخصی\n\n"
        "می‌توان AI را برای یک حوزه مشخص تنظیم کرد "
        "تا در تحلیل، برنامه‌ریزی و کارهای تکراری کمک کند.",

    "lesson20":
        "2️⃣0️⃣ تبدیل AI به مهارت واقعی\n\n"
        "هدف، حفظ کردن اسم ابزارها نیست.\n\n"
        "مهارت واقعی یعنی بتوانی یک مسئله را ببینی، "
        "راه‌حل مناسب پیدا کنی و از AI برای حل آن استفاده کنی.\n\n"
        "🚀 اینجا پایان مسیر نیست؛ شروع استفاده واقعی از AI است."
}


# ==================================================
# LESSON BACK MENU
# ==================================================

def lesson_back_menu(lesson_id):

    keyboard = InlineKeyboardMarkup()

    if lesson_id in [
        "lesson1",
        "lesson2",
        "lesson3",
        "lesson4",
        "lesson5"
    ]:
        back = "chapter1"

    elif lesson_id in [
        "lesson6",
        "lesson7",
        "lesson8",
        "lesson9",
        "lesson10"
    ]:
        back = "chapter2"

    elif lesson_id in [
        "lesson11",
        "lesson12",
        "lesson13",
        "lesson14",
        "lesson15"
    ]:
        back = "chapter3"

    else:
        back = "chapter4"

    keyboard.add(
        InlineKeyboardButton(
            text="🔙 بازگشت به فصل",
            callback_data=back
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🏠 منوی اصلی",
            callback_data="main"
        )
    )

    return keyboard


# ==================================================
# READY
# ==================================================

@bot.event
async def on_ready():

    print(f"{bot.user} is ready!")


# ==================================================
# MESSAGES
# ==================================================

@bot.event
async def on_message(message: Message):

    if message.content == "/start":

        await message.reply(
            "🤖 AIHOOOSH\n\n"
            "دنیای هوش مصنوعی، ساده و کاربردی.\n\n"
            "از آموزش تا اخبار، ابزارها و کاربردهای واقعی.\n\n"
            "👇 یک بخش را انتخاب کن:",
            components=main_menu()
        )

    elif message.content == "/learn":

        await message.reply(
            "🧠 AI از صفر تا کاربرد\n\n"
            "۲۰ قسمت در ۴ فصل.\n\n"
            "👇 فصل موردنظر را انتخاب کن:",
            components=learning_menu()
        )

    elif message.content == "/news":

        await message.reply(
            "⏳ در حال دریافت اخبار جدید..."
        )

        await message.reply(format_news())

    elif message.content == "/tools":

        await message.reply(
            "🛠 بانک ابزارهای AIHOOOSH\n\n"
            "ابزارها را بر اساس کاربرد دسته‌بندی کرده‌ایم.\n\n"
            "👇 یک دسته را انتخاب کن:",
            components=tools_menu()
        )

    elif message.content == "/usecases":

        await message.reply(
            "💡 کاربردهای واقعی AI\n\n"
            "این بخش به‌زودی با نمونه‌های واقعی و کاربردی تکمیل می‌شود."
        )

    elif message.content == "/roadmap":

        await message.reply(
            "🎯 مسیر یادگیری AI\n\n"
            "شناخت AI → پرامپت → ابزارها → کاربرد → سیستم‌سازی",
            components=learning_menu()
        )

    else:

        await message.reply(
            "برای شروع، /start را بزن. 🤖"
        )


# ==================================================
# CALLBACKS
# ==================================================

@bot.event
async def on_callback(callback: CallbackQuery):

    data = callback.data

    # ----------------------------------------------
    # MAIN
    # ----------------------------------------------

    if data == "main":

        await callback.message.reply(
            "🤖 AIHOOOSH\n\n"
            "👇 یک بخش را انتخاب کن:",
            components=main_menu()
        )

    # ----------------------------------------------
    # LEARNING
    # ----------------------------------------------

    elif data == "learn":

        await callback.message.reply(
            "🧠 AI از صفر تا کاربرد\n\n"
            "۲۰ قسمت در ۴ فصل.\n\n"
            "👇 فصل موردنظر را انتخاب کن:",
            components=learning_menu()
        )

    # ----------------------------------------------
    # NEWS
    # ----------------------------------------------

    elif data == "news":

        await callback.message.reply(
            "⏳ در حال دریافت جدیدترین اخبار AI..."
        )

        await callback.message.reply(
            format_news()
        )

    # ----------------------------------------------
    # TOOLS
    # ----------------------------------------------

    elif data == "tools":

        await callback.message.reply(
            "🛠 بانک ابزارهای AIHOOOSH\n\n"
            "ابزارها را بر اساس کاربرد دسته‌بندی کرده‌ایم.\n\n"
            "👇 یک دسته را انتخاب کن:",
            components=tools_menu()
        )

    elif data == "tool_text":

        await callback.message.reply(
            format_category("text"),
            components=tool_back_menu()
        )

    elif data == "tool_image":

        await callback.message.reply(
            format_category("image"),
            components=tool_back_menu()
        )

    elif data == "tool_video":

        await callback.message.reply(
            format_category("video"),
            components=tool_back_menu()
        )

    elif data == "tool_voice":

        await callback.message.reply(
            format_category("voice"),
            components=tool_back_menu()
        )

    elif data == "tool_research":

        await callback.message.reply(
            format_category("research"),
            components=tool_back_menu()
        )

    elif data == "tool_productivity":

        await callback.message.reply(
            format_category("productivity"),
            components=tool_back_menu()
        )

    # ----------------------------------------------
    # OTHER SECTIONS
    # ----------------------------------------------

    elif data == "usecases":

        await callback.message.reply(
            "💡 کاربردهای واقعی AI\n\n"
            "نمونه‌های واقعی و کاربردی به‌زودی اضافه می‌شوند."
        )

    elif data == "roadmap":

        await callback.message.reply(
            "🎯 مسیر یادگیری AI\n\n"
            "از شناخت AI تا استفاده حرفه‌ای.",
            components=learning_menu()
        )

    # ----------------------------------------------
    # CHAPTERS
    # ----------------------------------------------

    elif data == "chapter1":

        await callback.message.reply(
            "📘 فصل ۱ — آشنایی با AI\n\n"
            "👇 درس موردنظر را انتخاب کن:",
            components=chapter1_menu()
        )

    elif data == "chapter2":

        await callback.message.reply(
            "🧩 فصل ۲ — کار کردن با AI\n\n"
            "👇 درس موردنظر را انتخاب کن:",
            components=chapter2_menu()
        )

    elif data == "chapter3":

        await callback.message.reply(
            "🚀 فصل ۳ — استفاده واقعی\n\n"
            "👇 درس موردنظر را انتخاب کن:",
            components=chapter3_menu()
        )

    elif data == "chapter4":

        await callback.message.reply(
            "🎯 فصل ۴ — حرفه‌ای‌تر شدن\n\n"
            "👇 درس موردنظر را انتخاب کن:",
            components=chapter4_menu()
        )

    # ----------------------------------------------
    # LESSONS
    # ----------------------------------------------

    elif data in lessons:

        await callback.message.reply(
            lessons[data],
            components=lesson_back_menu(data)
        )


# ==================================================
# RUN
# ==================================================

bot.run()
