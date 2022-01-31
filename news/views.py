from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import UserFollowedStocks

# news Page Controller [ Karim Mohammed Aboelazm ] [05-04-2021]

@login_required
def stock_news(request):
    stock = UserFollowedStocks.objects.all()
    return  render(request, 'stock-news.html', {'stock':stock})

    
