from django.shortcuts import render
import datetime
import pytz

def get_period_icon(hour: int) -> str:
    """
    시간(hour)을 받아서 Bootstrap Icon 클래스를 반환합니다.
    - 아침(6~11): bi-sun
    - 점심(12~16): bi-sunrise
    - 저녁(17~20): bi-sunset
    - 밤(그 외): bi-moon
    """
    if 6 <= hour < 12:
        return 'bi-sun'
    elif 12 <= hour < 17:
        return 'bi-sunrise'
    elif 17 <= hour < 21:
        return 'bi-sunset'
    else:
        return 'bi-moon'

def index(request):
    zones = [
        ('서울Seoul', 'Asia/Seoul'),
        ('뉴욕NewYork', 'America/New_York'),
        ('런던London', 'Europe/London'),
        ('도쿄Tokyo', 'Asia/Tokyo'),
        ('상하이Shanghai', 'Asia/Shanghai'),
        ('베이징Beijing', 'Asia/Shanghai'),
        ('뉴델리NewDelhi', 'Asia/Kolkata'),
        ('뱅갈로르Bengaluru', 'Asia/Kolkata'),
        ('콜카타India', 'Asia/Kolkata'),
        ('카이로Cairo', 'Africa/Cairo'),
        ('케이프타운CapeTown', 'Africa/Johannesburg'),
        ('타이페이Taipei', 'Asia/Taipei'),
        ('로스앤젤레스LosAngeles', 'America/Los_Angeles'),
        ('오스틴Austin', 'America/Chicago'),
        ('워싱턴Washington', 'America/New_York'),
        ('UTC', 'UTC'),
    ]
    now_times = []
    for label, tz_name in zones:
        tz = pytz.timezone(tz_name)
        now_dt = datetime.datetime.now(tz)
        hour = now_dt.hour
        now_str = now_dt.strftime('%Y-%m-%d %H:%M:%S')
        icon = get_period_icon(hour)
        now_times.append({
            'label': label,
            'time': now_str,
            'icon': icon,
        })

    return render(request, 'worldtime/index.html', {
        'now_times': now_times
    })