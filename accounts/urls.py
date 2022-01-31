from django.urls import path
from django.urls.conf import include
from . import views
from .views import UserCreationForm, UserRegisterView
from django.contrib.auth.views import LoginView, LogoutView


app_name='accounts'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile', views.profile,name="profile"),
    path('delete/<int:id>',views.dell,name='delete'),
    path('edit_profile', views.edit_profile,name="edit_profile"),
    # path('api_accounts/',include('accounts.api.urls', namespace="accounts_api_return")),
    
]
