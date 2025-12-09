from django.db import models

class HomePage(models.Model):
    title = models.CharField(max_length=200)

    p1 = models.TextField()
    p2 = models.TextField()
    p3 = models.TextField()
    p4 = models.TextField()
    p5 = models.TextField()
    p6 = models.TextField()

    def __str__(self):
        return "Home Page"


class ServicesPage(models.Model):
    title = models.CharField(max_length=200)

    p1 = models.TextField()
    p2 = models.TextField()
    p3 = models.TextField()
    p4 = models.TextField()
    p5 = models.TextField()
    p6 = models.TextField()

    def __str__(self):
        return "Services Page"


class ContactPage(models.Model):
    title = models.CharField(max_length=200)

    p1 = models.TextField()
    p2 = models.TextField()
    p3 = models.TextField()
    p4 = models.TextField()
    p5 = models.TextField()
    p6 = models.TextField()

    def __str__(self):
        return "Contact Page"
