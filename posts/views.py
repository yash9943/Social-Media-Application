from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from . models import Posts, Likes, Comment
from django.urls import reverse_lazy
from django.contrib import messages
from . forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AddPost(CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('feed')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class FeedView(ListView):
    model = Posts
    queryset = Posts.objects.order_by('-created_at')
    template_name = 'feed.html'
    context_object_name = 'all_posts'
#     print(queryset)

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EditPost(UpdateView):
    model = Posts
    form_class = PostForm
    template_name = 'edit_post.html'
    success_url = reverse_lazy("feed")

    def get_queryset(self):
        post = Posts.objects.filter(user=self.request.user)
        return post

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DeletePost(DeleteView):
    model = Posts
    template_name = 'delete_post.html'
    success_url = reverse_lazy("feed")

    def get_queryset(self):
        post = Posts.objects.filter(user=self.request.user)
        return post
    
    
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class LikeCount(View):
    def post(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)

        like_obj, created = Likes.objects.get_or_create(user=request.user,post=post)
        if not created:
            like_obj.delete()
        return redirect('feed')
    
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CommentAdd(View):
    def post(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

        return redirect('feed')


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'edit_comment.html'
    success_url = reverse_lazy('feed')

    def get_queryset(self):
        # Only comment owner can edit
        return Comment.objects.filter(user=self.request.user)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CommentDelete(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('feed')

    def get_queryset(self):
        # Only comment owner can delete
        return Comment.objects.filter(user=self.request.user)

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CommentCount(View):
    def post(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)

        comment_obj, created = Comment.objects.get_or_create(user=request.user,post=post)
        if not created:
            comment_obj.delete()
        return redirect('feed')