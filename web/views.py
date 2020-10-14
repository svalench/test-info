from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from web.forms import CreateCorparation
from web.models import Corparations

@login_required
class Cabinet:
    def start(request):
        print(dir(request.user))
        return render(request, 'cabinet/cabinet.html', {
            'foo': 'bar',
        })
    def create_corp(request):
        if request.method == 'POST':
            try:
                cor = Corparations.objects.filter(user_id=request.user)
                form = CreateCorparation(request.POST, instance=cor[0])
            except:
                form = CreateCorparation(request.POST)
            if form.is_valid():
                res = form.save(commit=False)
                res.user_id = request.user
                res.save()
                return HttpResponseRedirect(reverse('cabinet'))
        else:
            try:
                cor = Corparations.objects.filter(user_id=request.user)
                if(cor[0]):
                    data = {'name':cor[0].name}
                else:
                    data = {}
            except:
                data = {}
            form = CreateCorparation(initial=data)
        return render(request,'cabinet/corp_create.html',{'form': form})