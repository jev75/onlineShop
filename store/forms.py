from django import forms
from .models import Review, Clothing, Color

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        labels = {
            'rating': 'Įvertinimas',
            'comment': 'Atsiliepimas'
        }
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

class ClothingForm(forms.ModelForm):
    class Meta:
        model = Clothing
        fields = ['name', 'category', 'genre', 'brand', 'description', 'price', 'sizes', 'colors', 'stock', 'is_on_sale', 'image']

    def __init__(self, *args, **kwargs):
        super(ClothingForm, self).__init__(*args, **kwargs)
        self.fields['colors'].queryset = Color.objects.all()
        self.fields['colors'].choices = [('', '----')] + [(color.id, color.name) for color in self.fields['colors'].queryset]
