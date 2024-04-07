from django import forms
from categories.models import Category
from django.core.validators import MinValueValidator

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter category description', 'rows': 3}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control d-none', 'id': 'image_input', 'onchange': 'previewImage(event)'})
        }


    def clean_name(self):
        name = self.cleaned_data['name']
        name_found = Category.objects.filter(name=name).exists()
        if name_found:
            raise forms.ValidationError('Title used before , please choose another one')
        if len(name) < 2:
            raise forms.ValidationError('Title length must be greater than 2 chars')
        return name
