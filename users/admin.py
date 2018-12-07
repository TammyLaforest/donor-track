from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import Profile, BusinessProfile

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# class CustomModelAdmin(admin.ModelAdmin):
#
#     def __init__(self, model, admin_site):
#         self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
#         super(CustomModelAdmin, self).__init__(model, admin_site)
#


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


admin.site.register(Profile)
admin.site.register(BusinessProfile)
