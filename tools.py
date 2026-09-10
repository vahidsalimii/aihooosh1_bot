# ==================================================
# AIHOOOSH TOOLS DATABASE
# ==================================================

TOOLS = {

    "text": {
        "title": "✍️ ابزارهای متن و تولید محتوا",
        "items": [

            {
                "name": "ChatGPT",
                "description": "نوشتن، ایده‌پردازی، تحلیل، آموزش و تولید محتوا",
                "url": "https://chatgpt.com/",
                "status": "شروع رایگان"
            },

            {
                "name": "Claude",
                "description": "نوشتن، تحلیل متن، خلاصه‌سازی و کار با اسناد",
                "url": "https://claude.ai/",
                "status": "پلن رایگان + پولی"
            },

            {
                "name": "Gemini",
                "description": "دستیار هوش مصنوعی برای تحقیق، نوشتن و ایده‌پردازی",
                "url": "https://gemini.google.com/",
                "status": "شروع رایگان"
            },

            {
                "name": "Perplexity",
                "description": "جستجو و تحقیق با کمک هوش مصنوعی",
                "url": "https://www.perplexity.ai/",
                "status": "پلن رایگان + پولی"
            }

        ]
    },


    "image": {
        "title": "🎨 ابزارهای تصویر و طراحی",
        "items": [

            {
                "name": "Canva AI",
                "description": "طراحی، تولید تصویر، پست، ارائه و محتوای بصری",
                "url": "https://www.canva.com/",
                "status": "شروع رایگان"
            },

            {
                "name": "Adobe Firefly",
                "description": "تولید و ویرایش تصاویر با هوش مصنوعی",
                "url": "https://firefly.adobe.com/",
                "status": "پلن رایگان + پولی"
            },

            {
                "name": "Leonardo AI",
                "description": "تولید تصاویر و محتوای بصری با AI",
                "url": "https://leonardo.ai/",
                "status": "پلن رایگان + پولی"
            },

            {
                "name": "Ideogram",
                "description": "تولید تصویر، مخصوصاً طراحی‌های دارای متن",
                "url": "https://ideogram.ai/",
                "status": "پلن رایگان + پولی"
            }

        ]
    },


    "video": {
        "title": "🎬 ابزارهای ویدئو",
        "items": [

            {
                "name": "Runway",
                "description": "تولید و ویرایش ویدئو با هوش مصنوعی",
                "url": "https://runwayml.com/",
                "status": "پلن رایگان + پولی"
            },

            {
                "name": "CapCut",
                "description": "تدوین ویدئو و ابزارهای AI برای محتوای شبکه‌های اجتماعی",
                "url": "https://www.capcut.com/",
                "status": "رایگان + امکانات پولی"
            },

            {
                "name": "Pika",
                "description": "ساخت ویدئو و انیمیشن از ایده و تصویر",
                "url": "https://pika.art/",
                "status": "پلن رایگان + پولی"
            },

            {
                "name": "HeyGen",
                "description": "ساخت ویدئو با آواتار و گوینده هوش مصنوعی",
                "url": "https://www.heygen.com/",
                "status": "پلن رایگان + پولی"
            }

        ]
    },


    "voice": {
        "title": "🎙 ابزارهای صدا",
        "items": [

            {
                "name": "ElevenLabs",
                "description": "تبدیل متن به صدا، صداگذاری، دوبله و ابزارهای صوتی",
                "url": "https://elevenlabs.io/",
                "status": "شروع رایگان"
            },

            {
                "name": "Canva Text to Speech",
                "description": "تبدیل متن به صدای مصنوعی داخل Canva",
                "url": "https://www.canva.com/",
                "status": "رایگان محدود + پولی"
            }

        ]
    },


    "research": {
        "title": "🔎 ابزارهای تحقیق و جستجو",
        "items": [

            {
                "name": "Perplexity",
                "description": "جستجوی هوشمند و تحقیق با کمک AI",
                "url": "https://www.perplexity.ai/",
                "status": "پلن رایگان + پولی"
            },

            {
                "name": "NotebookLM",
                "description": "تحلیل و پرسش‌وپاسخ بر اساس منابع و اسناد",
                "url": "https://notebooklm.google.com/",
                "status": "شروع رایگان"
            },

            {
                "name": "ChatGPT",
                "description": "تحقیق، تحلیل، مقایسه و پردازش اطلاعات",
                "url": "https://chatgpt.com/",
                "status": "شروع رایگان"
            }

        ]
    },


    "productivity": {
        "title": "⚡ بهره‌وری و کار",
        "items": [

            {
                "name": "Notion AI",
                "description": "مدیریت اطلاعات، یادداشت، برنامه‌ریزی و کار با AI",
                "url": "https://www.notion.com/product/ai",
                "status": "پلن رایگان + پولی"
            },

            {
                "name": "Gamma",
                "description": "ساخت ارائه، صفحه و محتوای بصری با AI",
                "url": "https://gamma.app/",
                "status": "پلن رایگان + پولی"
            },

            {
                "name": "Canva",
                "description": "طراحی، ارائه، اسناد، ویدئو و محتوای شبکه‌های اجتماعی",
                "url": "https://www.canva.com/",
                "status": "شروع رایگان"
            }

        ]
    }
}


def get_category(category):

    return TOOLS.get(category)


def format_category(category):

    data = get_category(category)

    if not data:
        return "ابزار موردنظر پیدا نشد."

    text = f"{data['title']}\n\n"

    for index, tool in enumerate(data["items"], start=1):

        text += f"{index}️⃣ {tool['name']}\n"
        text += f"💡 {tool['description']}\n"
        text += f"💳 {tool['status']}\n"
        text += f"🔗 {tool['url']}\n\n"

    text += "━━━━━━━━━━━━━━\n"
    text += "🤖 AIHOOOSH"

    return text
