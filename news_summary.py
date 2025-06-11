import openai
import requests
from datetime import datetime

# 🔐 GPT API 키 설정
openai.api_key = "your-openai-api-key"

# 📥 뉴스 가져오기 (예: 연합뉴스 RSS)
rss_url = "https://www.yonhapnewstv.co.kr/browse/rss?cat=91"
rss = requests.get(rss_url).text  # 실제로는 xml 파싱 필요

# 예시 뉴스 본문
news_text = "정부가 오늘 발표한 경제정책에 따르면..."

# 🤖 GPT 요약
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "뉴스 기사를 간결하게 요약해줘."},
        {"role": "user", "content": news_text}
    ]
)

summary = response['choices'][0]['message']['content']

# 📝 Markdown 저장
today = datetime.now().strftime("%Y-%m-%d")
with open(f"{today}-news-summary.md", "w", encoding="utf-8") as f:
    f.write(f"# 📅 {today} 뉴스 요약\n\n")
    f.write(summary)
