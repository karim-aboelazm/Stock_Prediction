from django import forms
from . models import StocksTickers
class StockForm(forms.ModelForm):
    class Meta:
       model = StocksTickers
       fields = '__all__'
       
       
       
       
       
       