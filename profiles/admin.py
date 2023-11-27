from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_phone_number', 'default_country', 'default_postcode') # noqa
    search_fields = ('user__username', 'default_phone_number', 'default_country', 'default_postcode') # noqa


admin.site.register(UserProfile, UserProfileAdmin)
