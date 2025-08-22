# dailyq/services.py
import datetime, hashlib
from .models import Question

def get_today_question(date: datetime.date, category: str|None=None):
    qs = Question.objects.filter(is_active=True)
    if category:
        qs = qs.filter(category=category)
    total = qs.count()
    if not total:
        return None
    # 날짜 기반 결정적 선택: YYYYMMDD 해시 → 인덱스
    seed = date.strftime("%Y%m%d").encode()
    idx = int(hashlib.md5(seed).hexdigest(), 16) % total
    return qs[idx]
