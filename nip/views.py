from django.shortcuts import render
import requests

def info(request):
    try:
        ip = requests.get('https://api.ipify.org').text
    except:
        ip = '조회 실패'
    ua = request.META.get('HTTP_USER_AGENT', 'Unknown')
    return render(request, 'nip/info.html', {'ip': ip, 'user_agent': ua})
