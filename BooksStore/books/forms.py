from django import forms
from books.models import Book
from categories.models import Category
from django.core.validators import MinValueValidator

class BookForm(forms.Form):
    image = forms.ImageField(label='Image', widget=forms.ClearableFileInput(attrs={'class': 'form-control d-none', 'id': 'image_input', 'onchange':'previewImage(event)'}))
    title = forms.CharField(max_length=255, label='Title', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter book title'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'select category'}))
    author = forms.CharField(max_length=255, label='Author', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter author name'}))
    price = forms.FloatField(label='Price', validators=[MinValueValidator(0)], widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}))
    pagesNo = forms.IntegerField(label='Page Numbers', validators=[MinValueValidator(1)], widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter page numbers'}))
    ISBN = forms.IntegerField(label='ISBN', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter ISBN'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 3}))

    def clean_title(self):
        title = self.cleaned_data['title']
        title_found = Book.objects.filter(title=title).exists()
        if title_found:
            raise forms.ValidationError('Title used before , please choose another one')
        if len(title) < 2:
            raise forms.ValidationError('Title length must be greater than 2 chars')
        return title

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'select category that book belongs to.'

# We can build forms based on model
class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter book title'}),
            'category': forms.Select(attrs={'class': 'form-control form-select', 'placeholder': 'select category'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter author name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price', 'step': '0.01'}),
            'pagesNo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter page numbers'}),
            'ISBN': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter ISBN'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 3}),
            # 'image': forms.FileInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control d-none', 'id': 'image_input', 'onchange': 'previewImage(event)'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'select category that book belongs to.'
        # self.fields['category'].empty_label = None # to hide ----- in first option