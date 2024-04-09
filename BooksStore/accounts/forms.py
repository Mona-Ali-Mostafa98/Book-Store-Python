from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from accounts.models import User

class RegisterForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


















# def RegisterForm(UserCreationForm):
#     if UserCreationForm.is_valid():
#         user = UserCreationForm
#         user.set_password(
#             UserCreationForm.cleaned_data["password"]
#         )
#
#
# from django import forms
# from django.contrib.auth.models import User
#
#
# class RegisterationForm(UserCreationForm):
#     class Meta:
#         model = User
#         # fields = '__all__'
#         fields = ('username', 'password1','password2', 'first_name', 'last_name', 'email')
#
#         email = forms.EmailField(
#             label=_("Email"),
#             max_length=254,
#             widget=forms.EmailInput(attrs={"autocomplete": "email"}),
#         )
#         username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
#
#         new_password2 = forms.CharField(
#             label=_("New password confirmation"),
#             strip=False,
#             widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
#         )
#
#         old_password = forms.CharField(
#             label=_("Old password"),
#             strip=False,
#             widget=forms.PasswordInput(
#                 attrs={"autocomplete": "current-password", "autofocus": True}
#             ),
#         )