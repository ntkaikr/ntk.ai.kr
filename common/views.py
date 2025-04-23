from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, 'common/404.html', {})

def server_error(request):
    #return render(request, 'common/500.html', status=500)
    return render(request, 'common/500.html', {})