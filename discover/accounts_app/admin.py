from django.contrib import admin
from django.contrib.admin import ModelAdmin


from accounts_app.models import (
    Profile
)


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = [
        'user',
        'date_of_birth',
        'photo'
    ]
    raw_id_fields = [
        'user'
    ]
    

