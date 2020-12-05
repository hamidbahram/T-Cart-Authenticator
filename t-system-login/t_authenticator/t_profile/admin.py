from django.contrib import admin
from t_profile.models import UserProfle


@admin.register(UserProfle)
class AdminUserProfile(admin.ModelAdmin):
    pass