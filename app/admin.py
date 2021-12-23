from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ProductModel,HotListModel

class HotListDashBoard(SummernoteModelAdmin):
    list_display = ('id', 'title', 'category', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 10
    summernote_fields = ('content', )

admin.site.register(HotListModel, HotListDashBoard)
admin.site.register(ProductModel)

# mo-zee
# 12345.z