from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags

from web.forms import SignUpForm, LoginForm
from django.core.mail import send_mail
from django.utils.translation import gettext as _


def startPage(request):
    print('start')
    return render(request, 'start/index.html', {
        'foo': 'bar',
    })


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        email = form.cleaned_data.get('email')
        user = authenticate(username=username, password=password)
        login(request, user)
        html_message = render_to_string('mail/mail.html', {'Head': 'Hi. Please confirm your email!',
                                                           'Body': 'You are registered on the spark portal. Confirm your mail!',
                                                           'button': 'Confirm',
                                                           'href': 'pumpskills.com'
                                                           })
        plain_message = strip_tags(html_message)
        send_mail(
            _('registration on the site'),
            plain_message,
            'pumpskills@yandex.by',
            [email],
            html_message = html_message,
            fail_silently=False,
        )
        return HttpResponseRedirect(reverse('cabinet'))
    else:
        form = SignUpForm()
    return render(request, 'login/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('cabinet'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('start'))
