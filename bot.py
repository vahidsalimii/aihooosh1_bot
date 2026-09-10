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


# =========================
# MAIN MENU
# =========================

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


# =========================
# LEARNING MENU
# =========================

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
            text="🔙 بازگشت به منوی اصلی",
            callback_data="main"
        )
    )

    return keyboard


# =========================
# CHAPTER 1
# =========================

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


# =========================
# CHAPTER 2
# =========================

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
            text="9️⃣ خطاهای رایج در استفاده از AI",
            callback_data="lesson9"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="🔟 گرفتن نتیجه بهتر از AI",
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


# =========================
# CHAPTER 3
# =========================

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
            text="1️⃣3️⃣ AI برای تحقیق و جستجو",
            callback_data="lesson13"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="1️⃣4️⃣ AI برای تصویر و طراحی",
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


# =========================
# CHAPTER 4
# =========================

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
            text="1️⃣9️⃣ ساخت دستیار شخصی AI",
            callback_data="lesson19"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text="2️⃣0️⃣ تبدیل AI به یک مهارت واقعی",
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


# =========================
# LESSON TEXTS
# =========================

lessons = {

    "lesson1":
        "1️⃣ هوش مصنوعی چیست؟\n\n"
        "AI یا هوش مصنوعی مجموعه‌ای از فناوری‌هاست "
        "که به کامپیوتر اجازه می‌دهد بعضی کارهایی را "
        "که معمولاً به توانایی انسانی نیاز دارند انجام دهد.\n\n"
        "مثلاً فهمیدن متن، تولید تصویر، تحلیل اطلاعات "
        "و پاسخ دادن به سؤال‌ها.\n\n"
        "🎯 هدف این دوره این است که AI را نه فقط بشناسیم، "
        "بلکه بتوانیم از آن استفاده کنیم.",

    "lesson2":
        "2️⃣ AI چگونه کار می‌کند؟\n\n"
        "مدل‌های AI با استفاده از حجم زیادی از داده‌ها "
        "الگوها را یاد می‌گیرند و بعد بر اساس ورودی ما "
        "پاسخ یا خروجی تولید می‌کنند.\n\n"
        "به زبان ساده:\n"
        "داده → یادگیری الگو → دریافت درخواست → تولید پاسخ",

    "lesson3":
        "3️⃣ مدل‌های هوش مصنوعی\n\n"
        "مدل‌های مختلف برای کارهای مختلف ساخته شده‌اند.\n\n"
        "📝 متن\n"
        "🖼 تصویر\n"
        "🎬 ویدئو\n"
        "🎙 صدا\n"
        "📊 تحلیل داده\n\n"
        "شناخت مدل مناسب، یکی از مهارت‌های مهم کار با AI است.",

    "lesson4":
        "4️⃣ تفاوت AI و ابزارهای AI\n\n"
        "AI یک فناوری یا قابلیت است.\n"
        "ابزار AI محصولی است که این فناوری را در اختیار ما قرار می‌دهد.\n\n"
        "مثلاً یک ابزار می‌تواند برای نوشتن، طراحی تصویر، "
        "ساخت ویدئو یا تحلیل اطلاعات از AI استفاده کند.",

    "lesson5":
        "5️⃣ از کجا شروع کنیم؟\n\n"
        "لازم نیست از روز اول همه چیز درباره AI بدانیم.\n\n"
        "مسیر درست:\n"
        "1. شناخت AI\n"
        "2. یادگیری درخواست درست\n"
        "3. استفاده از ابزارها\n"
        "4. حل مسائل واقعی\n"
        "5. ساخت سیستم کاری شخصی\n\n"
        "از اینجا به بعد وارد بخش عملی می‌شویم.",

    "lesson6":
        "6️⃣ چگونه با AI صحبت کنیم؟\n\n"
        "AI ذهن‌خوان نیست.\n"
        "هرچه درخواست ما واضح‌تر باشد، احتمال گرفتن "
        "نتیجه مناسب بیشتر می‌شود.\n\n"
        "هدف، صحبت پیچیده نیست؛ هدف، انتقال دقیق مسئله است.",

    "lesson7":
        "7️⃣ پرامپت چیست؟\n\n"
        "Prompt همان دستوری است که به AI می‌دهیم.\n\n"
        "یک پرامپت خوب معمولاً مشخص می‌کند:\n"
        "چه کاری؟\n"
        "برای چه کسی؟\n"
        "با چه اطلاعاتی؟\n"
        "با چه فرمتی؟",

    "lesson8":
        "8️⃣ ساخت پرامپت بهتر\n\n"
        "یک روش ساده:\n\n"
        "نقش + هدف + اطلاعات + محدودیت + خروجی موردنظر\n\n"
        "مثلاً به‌جای «یک متن بنویس» می‌توانیم "
        "موضوع، مخاطب، لحن و طول متن را مشخص کنیم.",

    "lesson9":
        "9️⃣ خطاهای رایج در استفاده از AI\n\n"
        "❌ درخواست خیلی مبهم\n"
        "❌ ندادن اطلاعات کافی\n"
        "❌ قبول کردن اولین پاسخ بدون بررسی\n"
        "❌ انتظار نتیجه عالی از یک دستور کوتاه\n\n"
        "AI ابزار قدرتمندی است، اما خروجی آن باید بررسی شود.",

    "lesson10":
        "🔟 گرفتن نتیجه بهتر از AI\n\n"
        "اگر نتیجه خوب نبود، سریع ابزار را عوض نکن.\n\n"
        "اول درخواستت را اصلاح کن.\n"
        "اطلاعات بیشتری بده.\n"
        "فرمت خروجی را مشخص کن.\n"
        "و از AI بخواه قبل از پاسخ، مسئله را دقیق بررسی کند.",

    "lesson11":
        "1️⃣1️⃣ AI در تولید محتوا\n\n"
        "AI می‌تواند در ایده‌پردازی، تحقیق، نوشتن، "
        "طراحی تصویر، ساخت ویدئو و بازنویسی کمک کند.\n\n"
        "اما ارزش واقعی زمانی ایجاد می‌شود که AI را "
        "داخل یک فرآیند محتوایی مشخص قرار دهیم.",

    "lesson12":
        "1️⃣2️⃣ AI در کسب‌وکار\n\n"
        "کاربردهای مهم:\n"
        "🔎 تحقیق بازار\n"
        "📝 تولید محتوا\n"
        "📊 تحلیل اطلاعات\n"
        "💬 ارتباط با مشتری\n"
        "⚙️ بهینه‌سازی فرآیندها\n\n"
        "AI قرار نیست فقط «کار بیشتری» تولید کند؛ "
        "می‌تواند بعضی کارها را سریع‌تر و بهتر کند.",

    "lesson13":
        "1️⃣3️⃣ AI برای تحقیق و جستجو\n\n"
        "به‌جای جستجوی ساده، می‌توان مسئله را دقیق تعریف کرد "
        "و از AI برای دسته‌بندی، مقایسه و خلاصه‌سازی اطلاعات استفاده کرد.\n\n"
        "البته اطلاعات مهم باید با منابع معتبر بررسی شوند.",

    "lesson14":
        "1️⃣4️⃣ AI برای تصویر و طراحی\n\n"
        "امروز می‌توان با AI ایده تصویری را به یک تصویر تبدیل کرد.\n\n"
        "برای نتیجه بهتر باید موضوع، سبک، ترکیب‌بندی، "
        "نور، محیط و جزئیات موردنظر را مشخص کنیم.",

    "lesson15":
        "1️⃣5️⃣ AI برای ویدئو و صدا\n\n"
        "AI می‌تواند در سناریو، تولید تصویر، صداگذاری، "
        "تدوین و بعضی مراحل تولید ویدئو کمک کند.\n\n"
        "ترکیب چند ابزار می‌تواند یک فرآیند کامل تولید محتوا بسازد.",

    "lesson16":
        "1️⃣6️⃣ ساخت سیستم کاری با AI\n\n"
        "استفاده حرفه‌ای یعنی AI را وارد فرآیند روزانه کنیم.\n\n"
        "مثلاً:\n"
        "ورودی → تحلیل → تولید → بررسی → اصلاح → خروجی\n\n"
        "این یعنی سیستم، نه استفاده تصادفی از ابزار.",

    "lesson17":
        "1️⃣7️⃣ ترکیب چند ابزار AI\n\n"
        "گاهی یک ابزار برای همه کارها مناسب نیست.\n\n"
        "می‌توان یک فرآیند ساخت که در آن هر ابزار "
        "یک قسمت مشخص را انجام دهد.",

    "lesson18":
        "1️⃣8️⃣ اتوماسیون با AI\n\n"
        "اتوماسیون یعنی بعضی مراحل تکراری را طوری طراحی کنیم "
        "که با دخالت کمتر انسان انجام شوند.\n\n"
        "این بخش یکی از مهم‌ترین مسیرهای آینده استفاده از AI است.",

    "lesson19":
        "1️⃣9️⃣ ساخت دستیار شخصی AI\n\n"
        "می‌توان AI را برای یک حوزه مشخص تنظیم کرد تا "
        "در کارهای تکراری، تحلیل اطلاعات، ایده‌پردازی و برنامه‌ریزی کمک کند.\n\n"
        "هرچه دستورالعمل و اطلاعات بهتر باشد، دستیار کاربردی‌تر می‌شود.",

    "lesson20":
        "2️⃣0️⃣ تبدیل AI به یک مهارت واقعی\n\n"
        "هدف نهایی این دوره حفظ کردن اسم ابزارها نیست.\n\n"
        "مهارت واقعی یعنی بتوانی یک مسئله را ببینی، "
        "راه‌حل مناسب را پیدا کنی و از AI برای حل آن استفاده کنی.\n\n"
        "🚀 اینجا پایان مسیر نیست؛ شروع استفاده واقعی از AI است."
}


# =========================
# READY
# =========================

@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")


# =========================
# START / COMMANDS
# =========================

@bot.event
async def on_message(message: Message):

    if message.content == "/start":

        await message.reply(
            "🤖 AIHOOOSH\n\n"
            "دنیای هوش مصنوعی، ساده و کاربردی.\n\n"
            "اینجا قرار است AI را بشناسیم، "
            "ابزارهای جدید را ببینیم و کاربرد واقعی آن را یاد بگیریم.\n\n"
            "👇 یک بخش را انتخاب کن:",
            components=main_menu()
        )

    elif message.content == "/learn":

        await message.reply(
            "🧠 AI از صفر تا کاربرد\n\n"
            "یک مسیر ۲۰ قسمتی در ۴ فصل.\n\n"
            "👇 فصل موردنظر را انتخاب کن:",
            components=learning_menu()
        )

    elif message.content == "/news":

        await message.reply(
            "🆕 اخبار هوش مصنوعی\n\n"
            "در این بخش جدیدترین اخبار مهم AI "
            "به زبان ساده منتشر خواهد شد."
        )

    elif message.content == "/tools":

        await message.reply(
            "🛠 ابزارهای جدید AI\n\n"
            "ابزارهای جدید را بر اساس کاربرد معرفی می‌کنیم."
        )

    elif message.content == "/usecases":

        await message.reply(
            "💡 کاربردهای واقعی AI\n\n"
            "اینجا AI را در دنیای واقعی بررسی می‌کنیم."
        )

    elif message.content == "/roadmap":

        await message.reply(
            "🎯 مسیر یادگیری AI\n\n"
            "شروع → شناخت AI → پرامپت → ابزارها → کاربرد → سیستم‌سازی",
            components=learning_menu()
        )

    else:

        await message.reply(
            "برای شروع، /start را بزن. 🤖"
        )


# =========================
# CALLBACKS
# =========================

@bot.event
async def on_callback(callback: CallbackQuery):

    data = callback.data

    # MAIN
    if data == "main":

        await callback.message.reply(
            "🤖 AIHOOOSH\n\n"
            "دنیای هوش مصنوعی، ساده و کاربردی.\n\n"
            "👇 یک بخش را انتخاب کن:",
            components=main_menu()
        )

    # LEARNING
    elif data == "learn":

        await callback.message.reply(
            "🧠 AI از صفر تا کاربرد\n\n"
            "۲۰ قسمت در ۴ فصل.\n\n"
            "👇 فصل موردنظر را انتخاب کن:",
            components=learning_menu()
        )

    # CHAPTERS
    elif data == "chapter1":

        await callback.message.reply(
            "📘 فصل ۱ — آشنایی با AI\n\n"
            "در این فصل با مفاهیم پایه آشنا می‌شویم.\n\n"
            "👇 درس را انتخاب کن:",
            components=chapter1_menu()
        )

    elif data == "chapter2":

        await callback.message.reply(
            "🧩 فصل ۲ — کار کردن با AI\n\n"
            "اینجا یاد می‌گیریم چگونه بهتر با AI کار کنیم.\n\n"
            "👇 درس را انتخاب کن:",
            components=chapter2_menu()
        )

    elif data == "chapter3":

        await callback.message.reply(
            "🚀 فصل ۳ — استفاده واقعی\n\n"
            "در این فصل AI را وارد کارهای واقعی می‌کنیم.\n\n"
            "👇 درس را انتخاب کن:",
            components=chapter3_menu()
        )

    elif data == "chapter4":

        await callback.message.reply(
            "🎯 فصل ۴ — حرفه‌ای‌تر شدن\n\n"
            "از استفاده ساده به ساخت سیستم و فرآیند می‌رسیم.\n\n"
            "👇 درس را انتخاب کن:",
            components=chapter4_menu()
        )

    # LESSONS
    elif data in lessons:

        await callback.message.reply(
            lessons[data],
            components=lesson_back_menu(data)
        )


# =========================
# LESSON BACK MENU
# =========================

def lesson_back_menu(lesson_id):

    keyboard = InlineKeyboardMarkup()

    if lesson_id in ["lesson1", "lesson2", "lesson3", "lesson4", "lesson5"]:
        back = "chapter1"

    elif lesson_id in ["lesson6", "lesson7", "lesson8", "lesson9", "lesson10"]:
        back = "chapter2"

    elif lesson_id in ["lesson11", "lesson12", "lesson13", "lesson14", "lesson15"]:
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


# =========================
# RUN BOT
# =========================

bot.run()
