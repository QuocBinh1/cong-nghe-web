from django import forms
from .models import Post
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('id','author','title', 'description', 'price', 'quantity' ,'category' ,'trademark' , 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tiêu Đề'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nội Dung'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Giá'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Số Lượng'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Loại'}),
            'trademark': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hiệu'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
    