from django.shortcuts import render


class Cabinet:
    def start(request):
        return render(request, 'cabinet/cabinet.html', {
            'foo': 'bar',
        })