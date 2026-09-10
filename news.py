# ==================================================
# AIHOOOSH NEWS ENGINE
# ==================================================

import feedparser
import html
import re
from datetime import datetime, timezone


# ==================================================
# NEWS SOURCES
# ==================================================

RSS_FEEDS = [

    {
        "name": "Ars Technica",
        "url": "https://feeds.arstechnica.com/arstechnica/technology-lab"
    },

    {
        "name": "The Verge",
        "url": "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml"
    },

    {
        "name": "TechCrunch",
        "url": "https://techcrunch.com/category/artificial-intelligence/feed/"
    },

    {
        "name": "MIT Technology Review",
        "url": "https://www.technologyreview.com/feed/"
    }
]


# ==================================================
# SETTINGS
# ==================================================

MAX_NEWS = 7

# فقط خبرهای چند روز اخیر
MAX_AGE_DAYS = 3


# ==================================================
# TEXT CLEANER
# ==================================================

def clean_text(text):

    if not text:
        return ""

    text = html.unescape(text)

    text = re.sub(
        r"<[^>]+>",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ==================================================
# DATE PARSER
# ==================================================

def get_entry_time(entry):

    try:

        if hasattr(entry, "published_parsed") and entry.published_parsed:

            dt = datetime(
                *entry.published_parsed[:6],
                tzinfo=timezone.utc
            )

            return dt

        if hasattr(entry, "updated_parsed") and entry.updated_parsed:

            dt = datetime(
                *entry.updated_parsed[:6],
                tzinfo=timezone.utc
            )

            return dt

    except Exception:

        pass

    return None


# ==================================================
# AGE CHECK
# ==================================================

def is_recent(entry):

    dt = get_entry_time(entry)

    if not dt:

        # اگر RSS تاریخ نداشت،
        # خبر را حذف نمی‌کنیم.
        return True

    now = datetime.now(timezone.utc)

    age = now - dt

    return age.days <= MAX_AGE_DAYS


# ==================================================
# DUPLICATE CHECK
# ==================================================

def normalize_title(title):

    title = title.lower()

    title = re.sub(
        r"[^a-z0-9\u0600-\u06ff\s]",
        "",
        title
    )

    title = re.sub(
        r"\s+",
        " ",
        title
    )

    return title.strip()


# ==================================================
# GET NEWS
# ==================================================

def get_latest_news(limit=MAX_NEWS):

    all_news = []

    seen_titles = set()

    for source in RSS_FEEDS:

        try:

            feed = feedparser.parse(
                source["url"]
            )

            for item in feed.entries:

                title = clean_text(
                    item.get("title", "")
                )

                link = item.get(
                    "link",
                    ""
                ).strip()

                summary = clean_text(
                    item.get(
                        "summary",
                        item.get("description", "")
                    )
                )

                if not title or not link:
                    continue

                if not is_recent(item):
                    continue

                normalized = normalize_title(title)

                if normalized in seen_titles:
                    continue

                seen_titles.add(normalized)

                all_news.append({

                    "title": title,

                    "link": link,

                    "summary": summary,

                    "source": source["name"],

                    "date": get_entry_time(item)

                })

        except Exception as error:

            print(
                f"News source error "
                f"({source['name']}): {error}"
            )


    # ==================================================
    # SORT BY DATE
    # ==================================================

    all_news.sort(
        key=lambda item: item["date"]
        if item["date"]
        else datetime.min.replace(
            tzinfo=timezone.utc
        ),
        reverse=True
    )


    return all_news[:limit]


# ==================================================
# SHORT SUMMARY
# ==================================================

def make_short_summary(summary):

    if not summary:
        return ""

    summary = summary.strip()

    # طول مناسب برای پیام بله
    if len(summary) > 280:

        summary = summary[:280]

        last_space = summary.rfind(" ")

        if last_space > 100:

            summary = summary[:last_space]

        summary += "..."

    return summary


# ==================================================
# FORMAT NEWS
# ==================================================

def format_news():

    news = get_latest_news()

    if not news:

        return (
            "🆕 آخرین اخبار هوش مصنوعی\n\n"
            "فعلاً خبر جدیدی دریافت نشد.\n\n"
            "چند دقیقه بعد دوباره امتحان کن."
        )


    text = "🆕 آخرین اخبار هوش مصنوعی\n\n"


    for index, item in enumerate(
        news,
        start=1
    ):

        text += (
            f"{index}️⃣ "
            f"{item['title']}\n"
        )

        text += (
            f"🏷 منبع: "
            f"{item['source']}\n"
        )


        summary = make_short_summary(
            item["summary"]
        )


        if summary:

            text += (
                f"💡 {summary}\n"
            )


        text += (
            f"🔗 {item['link']}\n\n"
        )

        text += "━━━━━━━━━━━━━━\n\n"


    text += "🤖 AIHOOOSH"

    return text
