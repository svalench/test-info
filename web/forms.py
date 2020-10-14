from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext as _

from web.models import Corparations


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'
        self.fields['username'].label = _('Your nickname')
        self.fields['password1'].label = _('Your password')
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({'class': 'form-control'})

    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({'class': 'form-control'})

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CreateCorparation(ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #user_id = forms.ModelChoiceField(queryset=User.objects.all(), disabled=True, empty_label='choise user')

    class Meta:
        model = Corparations
        fields = [ 'name']
