from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from web.forms import CreateCorparation


class Cabinet:
    def start(request):
        return render(request, 'cabinet/cabinet.html', {
            'foo': 'bar',
        })
    def create_corp(request):
        if request.method == 'POST':
            form = CreateCorparation(request.POST)
            if form.is_valid():
                res = form.save(commit=False)
                res.user_id = request.user
                res.save()
                return HttpResponseRedirect(reverse('cabinet'))
        else:
            data = {'user_id':request.user}
            form = CreateCorparation(initial=data)
        return render(request,'cabinet/corp_create.html',{'form': form})