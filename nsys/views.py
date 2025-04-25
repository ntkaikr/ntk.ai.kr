import psutil
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def sys_info(request):
    cpu_percent = psutil.cpu_percent(interval=0.5)
    virtual_mem = psutil.virtual_memory()
    disk_usage  = psutil.disk_usage('/')

    context = {
        'cpu_percent': cpu_percent,
        'total_mem':    virtual_mem.total,
        'used_mem':     virtual_mem.used,
        'mem_percent':  virtual_mem.percent,
        'total_disk':   disk_usage.total,
        'used_disk':    disk_usage.used,
        'disk_percent': disk_usage.percent,
    }
    return render(request, 'nsys/info.html', context)
