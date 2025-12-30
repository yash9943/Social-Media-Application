from django import forms
from account.models import User, Profile

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput, required=True)
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    con_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email','username','password','con_password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        con_password = cleaned_data.get('con_password')
        
        if password != con_password:
            self.add_error("con_password","Password or Confirm Password do not match.")
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email already Exist.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This Username already Taken.")
        return username
    
class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']
        
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'name', 'bio']