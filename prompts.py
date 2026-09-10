# ==================================================
# AIHOOOSH PROMPTS DATABASE
# ==================================================

PROMPTS = {

    "content": {
        "title": "📝 پرامپت‌های تولید محتوا",
        "items": [

            {
                "title": "ایده‌پردازی برای پست",
                "description": "گرفتن ایده‌های متفاوت برای تولید محتوای شبکه‌های اجتماعی",
                "prompt": """تو یک استراتژیست حرفه‌ای تولید محتوا هستی.

برای موضوع [موضوع]، 10 ایده محتوایی متفاوت و غیرکلیشه‌ای پیشنهاد بده.

مخاطب: [مخاطب]
پلتفرم: [اینستاگرام / تلگرام / بله / یوتیوب]
هدف: [آموزش / جذب مخاطب / فروش / برندینگ]

برای هر ایده:
1. عنوان جذاب
2. هوک اولیه
3. ایده اصلی
4. پیشنهاد CTA

ایده‌ها نباید تکراری یا کلیشه‌ای باشند."""
            },

            {
                "title": "بازنویسی حرفه‌ای متن",
                "description": "تبدیل یک متن ساده به متنی جذاب و طبیعی",
                "prompt": """متن زیر را بازنویسی کن.

هدف:
- طبیعی و انسانی باشد
- جذاب باشد
- کلیشه‌ای نباشد
- منظور اصلی حفظ شود
- برای مخاطب فارسی‌زبان روان باشد

لحن: [صمیمی / حرفه‌ای / آموزشی / فروش]

متن:
[متن خود را اینجا قرار بده]"""
            }

        ]
    },


    "image": {
        "title": "🎨 پرامپت‌های ساخت تصویر",
        "items": [

            {
                "title": "تصویر تبلیغاتی محصول",
                "description": "تبدیل عکس محصول به یک صحنه تبلیغاتی حرفه‌ای",
                "prompt": """Create a premium commercial advertising image using the provided product image.

Keep the product itself accurate and recognizable.

Scene:
[توضیح محیط]

Style:
Premium commercial photography, realistic, cinematic, elegant.

Lighting:
Professional studio lighting with realistic highlights and shadows.

Composition:
The product should be the main focus, centered or placed according to a professional advertising composition.

Background:
[توضیح پس‌زمینه]

Camera:
Professional product photography, shallow depth of field, high detail.

Do not change the product design, logo, shape or important details."""
            },

            {
                "title": "تبدیل عکس ساده به عکس حرفه‌ای",
                "description": "ارتقای یک عکس معمولی به تصویر حرفه‌ای",
                "prompt": """Transform the provided image into a professional high-end photograph.

Keep the main subject accurate and recognizable.

Improve:
- lighting
- composition
- background
- depth
- realism
- professional photography quality

Use natural shadows and realistic materials.

The result should look like a professionally photographed image, not an artificial AI-generated image."""
            }

        ]
    },


    "video": {
        "title": "🎬 پرامپت‌های ویدئو",
        "items": [

            {
                "title": "تبدیل تصویر به ویدئو",
                "description": "ایجاد حرکت طبیعی و سینمایی از یک تصویر",
                "prompt": """Animate the provided image into a short cinematic video.

Keep the main subject and environment consistent.

Camera movement:
Slow and smooth cinematic camera movement.

Motion:
Natural and realistic movement.

Lighting:
Maintain the original lighting and atmosphere.

Style:
Premium cinematic commercial.

Avoid:
- sudden movements
- distorted objects
- changing the identity of the subject
- unnatural motion

The result should feel like a real professionally filmed shot."""
            },

            {
                "title": "ساخت سناریوی ویدئوی تبلیغاتی",
                "description": "ساخت سناریوی کوتاه برای تبلیغ یک محصول",
                "prompt": """تو یک کارگردان و سناریونویس تبلیغاتی حرفه‌ای هستی.

برای محصول [نام محصول] یک ویدئوی تبلیغاتی کوتاه طراحی کن.

مدت:
[مثلاً 30 ثانیه]

مخاطب:
[مخاطب هدف]

هدف:
[فروش / معرفی / برندینگ]

سناریو را به صحنه‌های جدا تقسیم کن.

برای هر صحنه بنویس:
- تصویر
- حرکت دوربین
- حرکت سوژه
- متن روی تصویر
- صدا یا نریشن

شروع ویدئو باید در 3 ثانیه اول توجه مخاطب را جلب کند."""
            }

        ]
    },


    "business": {
        "title": "💼 پرامپت‌های کسب‌وکار",
        "items": [

            {
                "title": "تحلیل کسب‌وکار",
                "description": "بررسی وضعیت یک کسب‌وکار و پیدا کردن فرصت‌های بهبود",
                "prompt": """تو یک مشاور ارشد کسب‌وکار هستی.

کسب‌وکار زیر را تحلیل کن:

نوع کسب‌وکار:
[نوع کسب‌وکار]

محصول یا خدمت:
[محصول یا خدمت]

مخاطب:
[مخاطب]

بازار:
[بازار]

مشکلات فعلی:
[مشکلات]

تحلیل را در این بخش‌ها ارائه بده:

1. نقاط قوت
2. نقاط ضعف
3. فرصت‌ها
4. تهدیدها
5. مشکلات اصلی
6. فرصت‌های درآمدی
7. پیشنهادهای عملی

از توصیه‌های کلی و کلیشه‌ای خودداری کن."""
            },

            {
                "title": "ایده‌های درآمدی",
                "description": "پیدا کردن راه‌های جدید برای درآمدزایی از یک مهارت یا کسب‌وکار",
                "prompt": """بر اساس اطلاعات زیر، 10 ایده واقعی برای درآمدزایی پیشنهاد بده.

مهارت‌ها:
[مهارت‌ها]

تجربه:
[تجربه]

امکانات:
[امکانات]

سرمایه اولیه:
[سرمایه]

زمان قابل اختصاص:
[زمان]

برای هر ایده بنویس:
- مدل درآمدی
- مشتری هدف
- روش شروع
- هزینه اولیه تقریبی
- سختی اجرا
- مزیت رقابتی

ایده‌ها باید عملی و قابل اجرا باشند، نه رویاپردازانه."""
            }

        ]
    },


    "study": {
        "title": "🎓 پرامپت‌های یادگیری",
        "items": [

            {
                "title": "معلم شخصی",
                "description": "یادگیری یک موضوع به زبان ساده و مرحله‌به‌مرحله",
                "prompt": """تو معلم شخصی من هستی.

موضوع:
[موضوع]

سطح فعلی من:
[مبتدی / متوسط / پیشرفته]

موضوع را مرحله‌به‌مرحله آموزش بده.

قوانین:
- ابتدا ساده توضیح بده
- سپس مثال واقعی بزن
- بعد یک سؤال از من بپرس
- پاسخ من را بررسی کن
- اگر اشتباه کردم، دلیل اشتباه را توضیح بده
- تا زمانی که مفهوم را یاد نگرفته‌ام سراغ مرحله بعد نرو

از توضیحات پیچیده و غیرضروری خودداری کن."""
            },

            {
                "title": "خلاصه‌سازی برای امتحان",
                "description": "تبدیل متن درسی به خلاصه‌ای قابل مرور",
                "prompt": """متن زیر را برای مطالعه و مرور امتحان خلاصه کن.

قوانین:

1. نکات مهم را حذف نکن.
2. مطالب را دسته‌بندی کن.
3. اصطلاحات مهم را مشخص کن.
4. نکات حفظی را جدا کن.
5. در پایان 10 سؤال امتحانی طراحی کن.

متن:
[متن درسی]"""
            }

        ]
    },


    "research": {
        "title": "🔎 پرامپت‌های تحقیق",
        "items": [

            {
                "title": "تحقیق عمیق",
                "description": "بررسی یک موضوع از چند زاویه",
                "prompt": """درباره موضوع زیر یک تحقیق ساختاریافته انجام بده:

موضوع:
[موضوع]

ابتدا مسئله را تعریف کن.

سپس بررسی کن:
1. پیشینه
2. وضعیت فعلی
3. عوامل مؤثر
4. مزایا
5. معایب
6. دیدگاه‌های مختلف
7. داده‌ها و آمار مهم
8. نتیجه‌گیری

هرجا اطلاعات قطعی نیست، آن را مشخص کن.

برای اطلاعات مهم، منابع معتبر پیشنهاد بده."""
            }

        ]
    },


    "prompting": {
        "title": "🧠 پرامپت‌نویسی",
        "items": [

            {
                "title": "ساخت پرامپت حرفه‌ای",
                "description": "تبدیل یک درخواست ساده به پرامپت دقیق",
                "prompt": """درخواست ساده من را به یک پرامپت حرفه‌ای تبدیل کن.

درخواست:
[درخواست من]

پرامپت را با این ساختار طراحی کن:

1. نقش AI
2. هدف
3. اطلاعات زمینه‌ای
4. وظیفه
5. محدودیت‌ها
6. معیارهای کیفیت
7. فرمت خروجی

در صورت وجود ابهام، ابتدا آن را مشخص کن.

پرامپت نهایی را آماده کپی ارائه بده."""
            }

        ]
    }

}


# ==================================================
# FUNCTIONS
# ==================================================

def get_prompt_category(category):

    return PROMPTS.get(category)


def format_prompt_category(category):

    data = get_prompt_category(category)

    if not data:
        return "دسته موردنظر پیدا نشد."

    text = f"{data['title']}\n\n"

    for index, item in enumerate(data["items"], start=1):

        text += f"{index}️⃣ {item['title']}\n"
        text += f"💡 {item['description']}\n\n"

    text += "👇 برای دیدن پرامپت، شماره موردنظر را انتخاب کن."

    return text


def get_prompt(category, index):

    data = get_prompt_category(category)

    if not data:
        return None

    items = data["items"]

    if index < 0 or index >= len(items):
        return None

    return items[index]


def format_prompt(category, index):

    item = get_prompt(category, index)

    if not item:
        return "پرامپت موردنظر پیدا نشد."

    return (
        f"🧠 {item['title']}\n\n"
        f"💡 {item['description']}\n\n"
        f"📋 پرامپت آماده:\n\n"
        f"{item['prompt']}\n\n"
        f"━━━━━━━━━━━━━━\n"
        f"🤖 AIHOOOSH"
    )
