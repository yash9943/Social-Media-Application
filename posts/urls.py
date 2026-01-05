from django.urls import path
from . views import AddPost, EditPost, DeletePost, LikeCount, CommentAdd, CommentUpdate, CommentDelete
from django.conf import settings
from django.conf.urls.static import static

app_name = "posts"

urlpatterns = [
    path('add-post/', AddPost.as_view(), name="add_post"),
    path('edit-post/<pk>/', EditPost.as_view(), name="edit_post"),
    path('delete-post/<pk>/', DeletePost.as_view(), name="delete_post"),
    path('like/<int:pk>/', LikeCount.as_view(), name='posts_likes'),
    path('comment/add/<int:pk>/', CommentAdd.as_view(), name='add_comment'),
    path('comment/edit/<int:pk>/', CommentUpdate.as_view(), name='edit_comment'),
    path('comment/delete/<int:pk>/', CommentDelete.as_view(), name='delete_comment'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)