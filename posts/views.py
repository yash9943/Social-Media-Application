from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from . models import Posts
from django.urls import reverse_lazy
from django.contrib import messages
from . forms import PostForm, EditPostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AddPost(LoginRequiredMixin, CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('feed')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class FeedView(LoginRequiredMixin,ListView):
    model = Posts
    queryset = Posts.objects.order_by('-created_at')
    template_name = 'feed.html'
    context_object_name = 'all_posts'
#     print(queryset)

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EditPost(LoginRequiredMixin, UpdateView):
    model = Posts
    form_class = EditPostForm
    template_name = 'edit_post.html'
    success_url = reverse_lazy("feed")

    def get_queryset(self):
        post = Posts.objects.filter(user=self.request.user)
        return post

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DeletePost(LoginRequiredMixin, DeleteView):
    model = Posts
    template_name = 'delete_post.html'
    success_url = reverse_lazy("feed")

    def get_queryset(self):
        post = Posts.objects.filter(user=self.request.user)
        return post