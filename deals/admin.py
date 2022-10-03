from django.contrib import admin

from deals.models import Deal, Discount, Action

admin.site.register(Deal)
admin.site.register(Discount)
admin.site.register(Action)
