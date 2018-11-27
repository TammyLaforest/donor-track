from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'company',
        'last_name1',
        'first_name1',
        'last_name2',
        'first_name2',
        )

admin.site.register(Contact, ContactAdmin)
