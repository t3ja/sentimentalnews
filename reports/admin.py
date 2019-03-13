# Register your models here.
from django.contrib import admin
from .models import *


class ReportAdmin(admin.ModelAdmin):
    list_display = ['country', 'goodness', 'pub_date']

    # def current_bid_display(self, obj):
    #     return "£{0}".format(obj.current_bid)


admin.site.register(Report, ReportAdmin)
