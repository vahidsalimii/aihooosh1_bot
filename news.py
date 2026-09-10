import feedparser
import html
import re


RSS_FEEDS = [
    "https://feeds.arstechnica.com/arstechnica/technology-lab",
    "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml",
]


def clean_text(text):
    if not text:
        return ""

    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def get_latest_news(limit=5):

    all_news = []

    for url in RSS_FEEDS:

        try:
            feed = feedparser.parse(url)

            for item in feed.entries:

                title = clean_text(item.get("title", ""))
                link = item.get("link", "").strip()
                summary = clean_text(item.get("summary", ""))

                if not title or not link:
                    continue

                all_news.append({
                    "title": title,
                    "link": link,
                    "summary": summary
                })

        except Exception as error:
            print(f"News source error: {error}")

    return all_news[:limit]


def format_news():

    news = get_latest_news(5)

    if not news:
        return (
            "🆕 اخبار هوش مصنوعی\n\n"
            "فعلاً نتوانستم اخبار جدید را دریافت کنم.\n"
            "لطفاً چند دقیقه بعد دوباره امتحان کنید."
        )

    text = "🆕 آخرین اخبار هوش مصنوعی\n\n"

    for index, item in enumerate(news, start=1):

        text += f"{index}️⃣ {item['title']}\n"
        text += f"🔗 {item['link']}\n\n"

    text += "━━━━━━━━━━━━━━\n"
    text += "🤖 AIHOOOSH"

    return text
