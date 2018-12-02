# from django.http import HttpResponse
#
# import django_filters
# from .models import Contact
# from django.contrib.auth.models import User
#
#
# class ContactsNameFilter(django_filters.FilterSet):
#     class Meta:
#         model = Contact
#         user = User
#         fields = '__all__'
        # def get_filterset(self, *args, **kwargs):
        #     fs = super().get_filterset(*args, **kwargs)
        #     fs.filters['Owner'].field.queryset = fs.filters['owner'].field.queryset.filter(user=User)
        #     return fs
