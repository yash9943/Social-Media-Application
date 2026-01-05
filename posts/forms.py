from django import forms
from posts.models import Posts
from .models import Comment

class PostForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput, required=False)
    caption = forms.CharField(widget=forms.TextInput, required=False)
    
    class Meta:
        model = Posts
        fields = ['picture','caption']
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput)
    
    class Meta:
        model = Comment
        fields = ['content']
        