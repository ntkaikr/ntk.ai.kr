from django.shortcuts import render
import datetime
import pytz

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
        now = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
        now_times.append({'label': label, 'time': now})

    return render(request, 'worldtime/index.html', {
        'now_times': now_times
    })
