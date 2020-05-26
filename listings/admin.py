from django.contrib import admin
from . models import RegListing

# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','message' ,'list_date', 'reguser')
    list_display_links = ('id', 'title')
    list_filter = ('reguser',)
    search_fields = ('title', 'message')
    list_per_page = 25


admin.site.register(RegListing, ListingAdmin)