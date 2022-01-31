from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='home'
urlpatterns = [
    path('',views.main,name='home_page'),
    path('delete/<int:id>',views.dell,name='delete'),
    # apis
    # path('api_home/',include('home.api.urls',namespace="home_api")),
    # # 404
    # url(r'^$',views.main,name="Home"),
]

