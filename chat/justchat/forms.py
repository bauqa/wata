from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Book


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','desk','author',
        'book',
        'photo1','photo2','photo3')
        widgets = {
            "name":forms.TextInput(attrs={'class':'form-control'}),
            "desk":forms.Textarea(attrs={'class':'form-control'}),
            "author":forms.TextInput(attrs={'class':'form-control'}),
            "book":forms.FileInput(attrs={'class':'form-control'}),
        }