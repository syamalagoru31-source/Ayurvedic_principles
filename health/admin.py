from django.contrib import admin
from .models import Profile, Disease, Remedy, HealthTip

admin.site.register(Profile)
admin.site.register(Disease)
admin.site.register(Remedy)
admin.site.register(HealthTip)