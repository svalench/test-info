from django.shortcuts import render

def startPage(request):
    print('start')
    return render(request, 'start/index.html', {
        'foo': 'bar',
    })