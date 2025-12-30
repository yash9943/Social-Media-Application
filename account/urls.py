from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from account.views import UserLogin, HomePage, UserRegister, UserProfile, FeedView, UserLogout, UserEditProfile

urlpatterns = [
    path('',HomePage.as_view(),name='home_page'),
    path('login/', UserLogin.as_view(), name='login'),
    path('register/', UserRegister.as_view(), name='register'),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile/<pk>/', UserProfile.as_view(), name='profile'),
    path('edit-profile/', UserEditProfile.as_view(), name="edit_profile")
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
