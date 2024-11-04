from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(
        max_length=30,
        label='Введите логин',
        required=True
    )

    password = forms.CharField(
        min_length=8,
        label='Введите пароль',
        required=True
    )

    repeat_password = forms.CharField(
        min_length=8,
        label='Повторите пароль',
        required=True
    )

    age = forms.IntegerField(
        min_value=0,
        max_value=100,
        label='Введите свой возраст',
        required=True
    )
