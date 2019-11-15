from django.contrib import admin
from .models import Realtor, Immo

# Register your models here.
@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    pass

@admin.register(Immo)
class ImmoAdmin(admin.ModelAdmin):
    pass