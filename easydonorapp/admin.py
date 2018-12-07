from django.contrib import admin
from .models import Pledges, DepositSlip, Payments

admin.site.register(Pledges)
admin.site.register(DepositSlip)
admin.site.register(Payments)
