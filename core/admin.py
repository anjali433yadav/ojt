from django.contrib import admin
import core.translation

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import HomePage, ServicesPage, ContactPage


@admin.register(HomePage)
class HomePageAdmin(TranslationAdmin):
    pass


@admin.register(ServicesPage)
class ServicesPageAdmin(TranslationAdmin):
    pass


@admin.register(ContactPage)
class ContactPageAdmin(TranslationAdmin):
    pass
from django.contrib import admin




