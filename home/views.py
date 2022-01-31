from django.shortcuts import redirect, render,get_object_or_404
from .form import StockForm
from django.contrib.auth.decorators import login_required
from .models import StocksTickers
from accounts.models import UserFollowedStocks

@login_required
def main(request):
    import requests
    import json
    if request.method=='POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save() 
        return redirect('home:home_page')
    else:
        Data = StocksTickers.objects.all()
        followed_stock = []
        followed_stock_by_user = UserFollowedStocks.objects.all()
        
        # this is api for candle
        api_req_2 = requests.get("http://api.marketstack.com/v1/eod?access_key=8c161f1752b32b2c2287dbc21e905f4a&symbols=AAPL")
        api2 = json.loads(api_req_2.content)
        all_api=[]
        for j in api2["data"]:
            all_api.append([j['open'],j['high'],j['low'],j['close']]);
        for follow in followed_stock_by_user:
            followed_stock.append(follow)
        output = []
        my_ziplist = zip(Data,output)
        for ticker in Data:
            api_req = requests.get("https://cloud.iexapis.com/stable/stock/"+str(ticker)+"/quote?token=pk_5af932bd9cf7484ebce7bff7315546d9")
            try:
                api = json.loads(api_req.content)
                output.append(api)
            except Exception as e:
                api = "Error"
        context={'my_ziplist':my_ziplist,
                         'followed_stock':followed_stock,'all_api':all_api}
        return render(request, 'home.html', context)

@login_required
def dell(request,id):
    item = StocksTickers.objects.get(id=id)
    item.delete()
    return redirect('home:home_page')
