from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import HomePage, Service, ContactPage


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ("title_en", "title_fr", "title_de", "title_es")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title_en", "title_fr", "title_de", "title_es")
    search_fields = ("title_en", "title_fr")


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ("email", "phone")
