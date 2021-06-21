from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Fieldset, Layout, Submit
from accounts.models import User


class LoginForm(forms.Form):
    # username = forms.CharField(widget=forms.TextInput(
    #     attrs={'placeholder': 'Username'}))
    # password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={'placeholder': 'Password'}))
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    fields = ['username', 'password']

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_id = 'id-userForm'
        self.helper.form_method = 'POST'
        self.helper.form_action = 'login'
        self.helper.layout = Layout(
            Fieldset('Login', 'username', 'password', style='color:green;'),
            ButtonHolder(
                Submit('submit', 'Entra', css_class='btn-success')
            ))

    def get_user(self):
        username = self.cleaned_data.get('username').strip()
        password = self.cleaned_data.get('password')
        return authenticate(username=username, password=password)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    avatar = forms.ImageField()
    hobby = forms.CharField(max_length=50, required=False)
    sesso = forms.ChoiceField(
        choices=[('M', 'uomo'), ('F', 'donna')], required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name',
                  'last_name', 'avatar', 'hobby', 'sesso')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_id = 'id-userForm'
        # self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_action = 'signup'
        # self.helper.add_input(
        #     Submit('submit', 'Invia', css_class='btn-success'))
        self.helper.layout = Layout(
            Fieldset('Login Info', 'username', 'password1',
                     'password2', style='color:green;'),
            Fieldset('Profile', 'first_name', 'last_name', 'avatar',
                     'hobby', 'sesso', style='color:green;'),
            ButtonHolder(
                Submit('submit', 'Invia', css_class='btn-success')
            ))
