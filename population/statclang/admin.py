from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Population)

class PopulationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'nbre_habitant',)
    list_filter = ('nom',)