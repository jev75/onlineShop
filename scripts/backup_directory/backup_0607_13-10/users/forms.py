from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_form_control()

    def apply_form_control(self):
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('El. pašto adresas turi būti unikalus')
        return email

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_form_control()

    def apply_form_control(self):
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Toks el. paštas jau naudojamas sistemoje')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_form_control()
        self.fields['username'].widget.attrs.update({"placeholder": 'Sugalvokite savo prisijungimo vardą'})
        self.fields['email'].widget.attrs.update({"placeholder": 'Įveskite savo el. paštą'})
        self.fields['first_name'].widget.attrs.update({"placeholder": 'Jūsų vardas'})
        self.fields["last_name"].widget.attrs.update({"placeholder": 'Jūsų pavardė'})
        self.fields['password1'].widget.attrs.update({"placeholder": 'Sugalvokite savo slaptažodį'})
        self.fields['password2'].widget.attrs.update({"placeholder": 'Pakartokite sugalvotą slaptažodį'})

    def apply_form_control(self):
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Naudotojo vardas',
            'class': 'form-control',
            'autocomplete': 'off'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Naudotojo slaptažodis',
            'class': 'form-control',
            'autocomplete': 'off'
        })
        self.fields['username'].label = 'Vartotojo vardas'

class UserPasswordChangeForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_form_control()

    def apply_form_control(self):
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

