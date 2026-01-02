from django.shortcuts import render, redirect
from account.models import User, Profile
from django.views.generic import TemplateView, View, CreateView, UpdateView
from django.urls import reverse_lazy
from account.forms import RegistrationForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from posts.models import Posts

class HomePage(TemplateView):
    template_name = 'base.html'

class UserLogin(View):
    template_name = 'login.html'
    success_url = reverse_lazy('feed')
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,username=email,password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect(self.success_url)
        else:
            messages.error(request, "Invalid email or password")
            return render(request, self.template_name)
    
class UserRegister(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = User()
            data.email = form.cleaned_data['email']
            data.username = form.cleaned_data['username']
            data.set_password(form.cleaned_data['password'])
            data.save()
            messages.success(request, "User Register Succesfully.")
            return redirect('login') 
        else:
            print("Form not valid", form.errors)
        return render(request, self.template_name, {"form":form})
        

class UserLogout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserProfile(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_post = Posts.objects.filter(user = self.request.user)
        profile, created = Profile.objects.get_or_create(user = self.request.user)
        context['profile'] = profile
        context['user_post'] = user_post
        return context
    

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserEditProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = "edit_profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
        