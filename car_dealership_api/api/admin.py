from django.contrib import admin
from .models import DealerLocation, Car, Version, Feature

# Register your models here.
admin.site.register(DealerLocation)
admin.site.register(Car)
admin.site.register(Version)
admin.site.register(Feature)

