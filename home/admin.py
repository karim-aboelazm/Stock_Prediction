from django.contrib import admin
from .models import StocksTickers
# Register your models here.
admin.site.register(StocksTickers)

class StocksTickers(admin.ModelAdmin):
    list_display = ('ticker','created_by','created_at')
    actions = None

    def save_model(self, request, obj):
        if not obj.created_by:
            obj.created_by = request.user.id
        obj.save()
        
        
        
        
        