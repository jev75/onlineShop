from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = []  # If you need additional fields, add them here

class BankTransferForm(forms.Form):
    PAYMENT_CHOICES = [
        ('paysera', 'Paysera sąskaita'),
        ('swedbank', 'AB "Swedbank" bankas'),
        ('seb', 'AB bankas "SEB"'),
        ('luminor', 'Luminor'),
        ('siauliu', 'AB "Šiaulių bankas"'),
        ('revolut', 'Revolut (LT)'),
        ('citadele', 'AS "Citadele bankas"'),
        ('urbo', 'UAB Urbo bankas'),
        ('lku', 'Lietuvos centrinė kredito unija'),
        ('n26', 'N26 Bank (LT)'),
    ]

    IMAGE_MAP = {
        'paysera': '/static/images/paysera.png',
        'swedbank': '/static/images/swedbank.png',
        'seb': '/static/images/seb.png',
        'luminor': '/static/images/luminor.png',
        'siauliu': '/static/images/siauliu.png',
        'revolut': '/static/images/revolut.png',
        'citadele': '/static/images/citadele.png',
        'urbo': '/static/images/urbo.png',
        'lku': '/static/images/lku.png',
        'n26': '/static/images/n26.png',
    }

    full_name = forms.CharField(
        label='Pilnas vardas',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Įveskite pilną vardą'
        })
    )
    email = forms.EmailField(
        label='El. paštas',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Įveskite el. paštą'
        })
    )
    phone = forms.CharField(
        label='Telefono numeris',
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Įveskite telefono numerį'
        })
    )
    address = forms.CharField(
        label='Adresas',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Įveskite adresą',
            'rows': 4,
            'cols': 40
        })
    )
    payment_method = forms.ChoiceField(
        label='Apmokėjimo būdas',
        choices=PAYMENT_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'payment-method'})
    )
