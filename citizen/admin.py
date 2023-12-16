from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Reporter, Pothole, Workorder, DamageFile

admin.site.register(Reporter)
admin.site.register(Pothole)
admin.site.register(Workorder)
admin.site.register(DamageFile)
