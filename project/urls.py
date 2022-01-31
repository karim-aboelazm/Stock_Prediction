from django.contrib import admin
from django.urls import path,include
from splash.views import splash
from django.conf import settings
from django.conf.urls.static import static
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',splash),
    path('home/', include('home.urls',namespace="home")),
    path('about-us/', include('about_us.urls',namespace="about-us")),
    path('accounts/', include('accounts.urls',namespace="accounts")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('news/', include('news.urls',namespace="news")), 
    
    
    
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
    #     name='password_change_done'),

    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
    #     name='password_change'),

    # path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
    #  name='password_reset_done'),

    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    #  name='password_reset_complete'),
    
  path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "registration/reset_password.html"), name ='reset_password'),
  path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"), name ='password_reset_done'),
  path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_form.html"), name ='password_reset_confirm'),
  path('complete_password_reset/', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_complete.html"), name ='password_reset_complete'),
  path('password_change', views.change_password, name='change_password'),
]


urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)