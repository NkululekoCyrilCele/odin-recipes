from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class AboutPage(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class HomePage(models.Model):
    header = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img/', storage=FileSystemStorage(
        location=settings.STATIC_ROOT, base_url=settings.STATIC_URL), null=True)
    recipes = models.ManyToManyField(Recipe)
    about_page = models.ForeignKey(AboutPage, on_delete=models.CASCADE)

    class Meta:
        ordering = ('header', )

    def __str__(self):
        return self.header
