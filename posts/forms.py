from django import forms
from posts.models import Posts

class PostForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput, required=False)
    caption = forms.CharField(widget=forms.TextInput, required=False)
    
    class Meta:
        model = Posts
        fields = ['picture','caption']
        
class EditPostForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput, required=False)
    caption = forms.CharField(widget=forms.TextInput, required=False)
    
    class Meta:
        model = Posts
        fields = ['picture','caption']