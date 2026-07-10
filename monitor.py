import os
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

URL = "https://m.smartstore.naver.com/moncolle_korea/products/13172025815"

html = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
).text

if "품절되었습니다" not in html:
    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": "🚨 포켓몬 카드 151 재입고 가능성 발견! 지금 확인해보세요.\n" + URL
        }
    )
