import psutil
import socket
import platform
import os
import time
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime

@staff_member_required
def sys_info(request):
    # 1) CPU
    cpu_percent = psutil.cpu_percent(interval=0.5)
    cpu_per_core = psutil.cpu_percent(interval=0.5, percpu=True)

    # 2) 메모리
    virtual_mem = psutil.virtual_memory()

    # 3) 디스크
    disk_usage = psutil.disk_usage('/')

    # 4) OS / 호스트 / 내부 IP
    os_name    = platform.system()
    os_version = platform.version()
    hostname   = socket.gethostname()
    try:
        internal_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        internal_ip = '알 수 없음'

    # 5) 서버 가동 시간 (Uptime)
    boot_ts = psutil.boot_time()
    uptime_s = time.time() - boot_ts
    uptime = str(datetime.utcfromtimestamp(uptime_s).strftime("%H:%M:%S"))

    # 6) 네트워크 인터페이스 & 트래픽
    net_addrs   = psutil.net_if_addrs()
    net_io      = psutil.net_io_counters(pernic=True)

    # 7) 프로세스 수
    proc_count = len(psutil.pids())

    # 8) 로드 애버리지 (Unix 계열)
    try:
        load1, load5, load15 = psutil.getloadavg()
    except AttributeError:
        load1 = load5 = load15 = None

    # 9) 파일 시스템 파티션별 사용량
    partitions = []
    for part in psutil.disk_partitions():
        usage = psutil.disk_usage(part.mountpoint)
        partitions.append({
            'mount': part.mountpoint,
            'total': usage.total,
            'used':  usage.used,
            'percent': usage.percent,
        })

    # 10) 주요 환경 변수 (예시)
    env_vars = {
        'DJANGO_SETTINGS_MODULE': os.environ.get('DJANGO_SETTINGS_MODULE'),
        'PATH': os.environ.get('PATH'),
    }

    context = {
        'cpu_percent': cpu_percent,
        'cpu_per_core': cpu_per_core,
        'total_mem': virtual_mem.total,
        'used_mem': virtual_mem.used,
        'mem_percent': virtual_mem.percent,
        'total_disk': disk_usage.total,
        'used_disk': disk_usage.used,
        'disk_percent': disk_usage.percent,
        'os_name': os_name,
        'os_version': os_version,
        'hostname': hostname,
        'internal_ip': internal_ip,
        'uptime': uptime,
        'net_addrs': net_addrs,
        'net_io': net_io,
        'proc_count': proc_count,
        'load1': load1,
        'load5': load5,
        'load15': load15,
        'partitions': partitions,
        'env_vars': env_vars,
    }
    return render(request, 'nsys/info.html', context)
