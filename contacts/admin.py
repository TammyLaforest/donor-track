from django.contrib import admin

from .models import Contact



# from contacts.models import Contact
#
# class ContactAdmin(admin.ModelAdmin):
#     list_display = (
#         'uuid',
#         'Company',
#         'Last_Name1',
#         'First_Name1',
#         'Last_Name2',
#         'First_Name2',
#         )

admin.site.register(Contact)
