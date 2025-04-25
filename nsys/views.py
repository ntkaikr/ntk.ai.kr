import psutil
import socket
import platform
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def sys_info(request):
    # CPU / 메모리 / 디스크
    cpu_percent = psutil.cpu_percent(interval=0.5)
    virtual_mem = psutil.virtual_memory()
    disk_usage  = psutil.disk_usage('/')

    # 운영체제 / 호스트 / 내부 IP
    os_name    = platform.system()       # e.g. 'Linux', 'Windows'
    os_version = platform.version()      # OS 버전
    hostname   = socket.gethostname()    # 서버 호스트명
    try:
        internal_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        internal_ip = '알 수 없음'

    context = {
        'cpu_percent': cpu_percent,
        'total_mem':    virtual_mem.total,
        'used_mem':     virtual_mem.used,
        'mem_percent':  virtual_mem.percent,
        'total_disk':   disk_usage.total,
        'used_disk':    disk_usage.used,
        'disk_percent': disk_usage.percent,
        'os_name':      os_name,
        'os_version':   os_version,
        'hostname':     hostname,
        'internal_ip':  internal_ip,
    }
    return render(request, 'nsys/info.html', context)
