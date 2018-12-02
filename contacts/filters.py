from django.http import HttpResponse

import django_filters
from .models import Contact
from django.contrib.auth.models import User


class ContactsNameFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        user = User
        fields = ('Last_Name1','First_Name1', 'Last_Name2', 'First_Name2', 'Company')
        # def get_filterset(self, *args, **kwargs):
        #     fs = super().get_filterset(*args, **kwargs)
        #     fs.filters['owner'].field.queryset = fs.filters['owner'].field.queryset.filter(user=User)
        #     return fs
