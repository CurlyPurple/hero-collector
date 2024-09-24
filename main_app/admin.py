from django.contrib import admin
# import your models here
from .models import Hero, Training, Workout

# Register your models here
admin.site.register(Hero)
admin.site.register(Training)
admin.site.register(Workout)