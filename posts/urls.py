from django.urls import path
from . views import AddPost, EditPost, DeletePost
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add-post/', AddPost.as_view(), name="add_post"),
    path('edit-post/<pk>/', EditPost.as_view(), name="edit_post"),
    path('delete-post/<pk>/', DeletePost.as_view(), name="delete_post"),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)