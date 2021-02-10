from django import forms
from .widgets import CustomClearableFileInput2
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

        image = forms.ImageField(label='Image',
                                 required=False,
                                 widget=CustomClearableFileInput2)
