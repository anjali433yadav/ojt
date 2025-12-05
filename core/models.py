from django.db import models
from django.utils.translation import gettext_lazy as _

# -------------------------
# COMMON BASE MODEL
# -------------------------
class TranslatedContent(models.Model):
    title_en = models.CharField(max_length=255, blank=True, null=True)
    title_fr = models.CharField(max_length=255, blank=True, null=True)
    title_de = models.CharField(max_length=255, blank=True, null=True)
    title_es = models.CharField(max_length=255, blank=True, null=True)

    text_en = models.TextField(blank=True, null=True)
    text_fr = models.TextField(blank=True, null=True)
    text_de = models.TextField(blank=True, null=True)
    text_es = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


# -------------------------
# HOME PAGE MODEL
# -------------------------
class HomePage(TranslatedContent):
    banner_image = models.ImageField(upload_to="home/", blank=True, null=True)

    def __str__(self):
        return f"Home Page Content"


# -------------------------
# SERVICES MODEL
# -------------------------
class Service(TranslatedContent):
    icon = models.CharField(max_length=100, blank=True, null=True)  # optional

    def __str__(self):
        return self.title_en or "Service"


# -------------------------
# CONTACT PAGE MODEL
# -------------------------
class ContactPage(TranslatedContent):
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "Contact Page Content"

