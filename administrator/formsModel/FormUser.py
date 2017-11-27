from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
class FormUser(forms.ModelForm):

    def save(self, commit=True):
        user = super(FormUser, self).save(commit=False)
        user.email = self.cleaned_data["username"]
        user.set_password((self.cleaned_data["password"]))
        if commit:
            user.save()
        return user

    class Meta :
        model = User
        fields  = ['username','first_name', 'password']
        widgets = {
            'username': forms.EmailInput(attrs={'class' : 'validate'}),
            'first_name': forms.TextInput(attrs={'class' : 'validate'}),
            'password': forms.PasswordInput(attrs={'class' : 'validate'})
        }

        error_messages = {
            'username' : {
                'require' : 'Username e obrigatorio.'
            },
            'first_name': {
                'require': 'Nome e obrigatorio.'
            },
            'password': {
                'require': 'Senha e obrigatorio.'
            },


        }




