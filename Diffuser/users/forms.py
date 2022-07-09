from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:     #class meta gives us a nested namespace for configurations and keeps the configurations in one place
        model = User  #the model that will be affected is user model, meaning when we do form.save() it is going to save it in the user model
        fields = ['username', 'email', 'password1', 'password2']