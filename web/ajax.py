from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

from web.models import Depatments


@login_required
def update_data_user(request):
    user = User.objects.get(pk=request.user.pk)
    if(request.POST['name']=='username'):
        try:
            user.username = request.POST['value']
            user.save()
        except:
            return JsonResponse({'text': 'error! This name is exist'},status=500)
    elif(request.POST['name']=='first_name'):
        user.first_name = request.POST['value']
    elif (request.POST['name'] == 'last_name'):
        user.last_name = request.POST['value']
    elif (request.POST['name'] == 'email'):
        user.email = request.POST['value']
    else:
        return JsonResponse({'text': 'error'})
    try:
        user.save()
    except:
        return JsonResponse({'text': 'error! Somthis wrong on server'}, status=500)
    return JsonResponse({'text': 'success'})

@login_required
def get_departments(request):
    try:
        deps = request.user.corparations_set.all()[0].departments_set.all()
    except:
        deps = 'null'
    return JsonResponse({'deps': deps})


@login_required
def create_or_update_departments(request):
    deps = request.user.corparations.depatments_set.all()
    print(deps)
    if(not deps):
        form = request.POST

        for i in form:
            print(form)
            a = Depatments(name=form['dat[0][a]'], corp_id_id=form['dat[0][b]'])
            a.save()
    return JsonResponse({'text': 'sucees load data'})