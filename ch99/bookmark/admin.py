from django.contrib import admin
from bookmark.models import Bookmark
# Register your models here.

@admin.register(Bookmark) #decorator
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')

#decorator 대신 admin.site.register(Bookmark,BookmarkAdmin)