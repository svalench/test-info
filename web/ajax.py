from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

@login_required
def update_data_user(request):
    user = User.objects.get(pk=request.user.pk)
    if(request.POST['name']=='username'):
        user.username = request.POST['value']
    elif(request.POST['name']=='first_name'):
        user.first_name = request.POST['value']
    elif (request.POST['name'] == 'last_name'):
        user.last_name = request.POST['value']
    elif (request.POST['name'] == 'email'):
        user.email = request.POST['value']
    else:
        return JsonResponse({'text': 'error'})
    user.save()
    return JsonResponse({'text': 'success'})
