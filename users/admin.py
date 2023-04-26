from django.contrib import admin
from users import models



# Register your models here.



class UserAdmin(admin.ModelAdmin):
    list_display = ["email", 'is_superuser']
    list_editable = ["is_superuser"]
    fieldsets = [
        (None, {"fields": ["email", "password", 'first_name', 'date_joined']}),
    ]
    search_fields = ["email"]
    ordering = ["email"]


admin.site.register(models.CustomUser, UserAdmin)
