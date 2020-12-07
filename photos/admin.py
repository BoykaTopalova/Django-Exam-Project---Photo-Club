from django.contrib import admin

# Register your models here.
from photos.models import Photo, Like, Comment


# Register your models here.

# class LikeInLine(admin.TabularInline):
#     model = Like


class PhotoAdmin(admin.ModelAdmin):
    # fields = ('type', 'title')
    list_display = ('id', 'type', 'title', 'data',)
    list_filter = ('type',)

    # inlines = (
    #     LikeInLine,
    # )


admin.site.register(Photo)
admin.site.register(Like)
admin.site.register(Comment)
