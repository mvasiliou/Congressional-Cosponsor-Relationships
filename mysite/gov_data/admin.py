from django.contrib import admin
from .models import Bill, Cosponsorship, Senator
# Register your models here.
admin.site.register(Bill)
admin.site.register(Senator)
admin.site.register(Cosponsorship)