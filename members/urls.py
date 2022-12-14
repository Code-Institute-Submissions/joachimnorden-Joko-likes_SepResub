from django.urls import path
from .views import (UserRegisterView, UserEditView, PasswordsChangeView,
                    ShowProfilePageView, EditProfilePageView,
                    CreateProfilePageView)
from . import views


urlpatterns = [
    path('register/', UserRegisterView.as_view(),
         name='register'),
    path('edit-settings/', UserEditView.as_view(),
         name='edit-settings'),
    path('password/', PasswordsChangeView.as_view(
        template_name='registration/change-password.html')),
    path('password-success', views.password_success,
         name='password-success'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(),
         name='show-profile'),
    path('<int:pk>/edit-profile-page', EditProfilePageView.as_view(),
         name='edit-profile-page'),
    path('create-profile-page', CreateProfilePageView.as_view(),
         name='create-profile-page'),
]
