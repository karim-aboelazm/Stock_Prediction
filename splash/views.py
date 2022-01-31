from django.shortcuts import render
# Create your views here.
def splash(request):
    return render(request,'splash.html', {})