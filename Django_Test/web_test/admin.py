from django.contrib import admin
from .models import *
# Register your models here.
class stcok_me_1(admin.ModelAdmin):
    list_display=['Stock_ID',
                  'Stock_name',
                  'category',
                  'socrce','Stock_remark']
    list_filter=['Stock_ID']
    list_editable=['Stock_name','category',
                  'socrce','Stock_remark']

admin.site.register(Stock_Me,stcok_me_1)
admin.site.register(Local_stock)
admin.site.register(profile)
admin.site.register(img_product)
admin.site.register(upload_document)

