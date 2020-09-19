from django.contrib import admin
from start_my_app.models import UserPosts


class AdminUserPost(admin.ModelAdmin):
    list_display = ('name', 'date_time', 'data', 'category')
    list_editable = ('data',)


# Register your models here.
admin.site.register(UserPosts, AdminUserPost)

