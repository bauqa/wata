from django.contrib import admin
from .models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','time_update','likenolike')
    list_display_links= ('id','name')
    search_fields= ('name','author')
    list_filter= ('likenolike', 'time_update')

admin.site.register(Book,BookAdmin)