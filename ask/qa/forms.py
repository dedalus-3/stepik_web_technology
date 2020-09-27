from django import forms
from django.contrib.auth.models import User
from .models import Answer, Question


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']

    def clean(self):
        return self.cleaned_data

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question', 'author']
        widgets = {'question': forms.HiddenInput(),
                   'author': forms.HiddenInput()}

    def clean(self):
        return self.cleaned_data

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}

    def clean(self):
        return self.cleaned_data

class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)

    def clean(self):
        return self.cleaned_data

    def save(self):
        pass

