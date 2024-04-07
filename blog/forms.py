from django import forms
from .models import Post
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'content', 'image')
        widgets = {'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
}