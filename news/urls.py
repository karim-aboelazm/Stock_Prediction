from django.urls import path,include
from . import views

app_name='news'
urlpatterns = [
    path('',views.stock_news,name="stock_news"),
    path('stock-news-api/list',include('news.api.urls',namespace="news_api")),
]





