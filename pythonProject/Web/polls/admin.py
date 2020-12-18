from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Occupations)
admin.site.register(Employees)
admin.site.register(AdditionalServices)
admin.site.register(CarBrands)
admin.site.register(Cars)
admin.site.register(Clients)
admin.site.register(Rent)

