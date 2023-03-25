from django.contrib import admin
from .models import Daily_mission, Weekly_mission, Nomal_mission

# Register your models here.
admin.site.register(Daily_mission)
admin.site.register(Weekly_mission)
admin.site.register(Nomal_mission)