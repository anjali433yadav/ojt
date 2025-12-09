from modeltranslation.translator import register, TranslationOptions
from .models import HomePage, ServicesPage, ContactPage


@register(HomePage)
class HomePageTranslationOptions(TranslationOptions):
    fields = ('title', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6')


@register(ServicesPage)
class ServicesPageTranslationOptions(TranslationOptions):
    fields = ('title', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6')


@register(ContactPage)
class ContactPageTranslationOptions(TranslationOptions):
    fields = ('title', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6')
