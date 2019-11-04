from django.conf import settings
from django.db import models
from django.utils import timezone


class Volume(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Text(models.Model):
    text_clip = models.TextField()
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)

    def __str__(self):
        return self.text_clip


class Image(models.Model):
    image_name = models.CharField(max_length=200)
    image_description = models.CharField(max_length=250)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

class Spanish(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class TextSpanish(models.Model):
    text_clip = models.TextField()
    volume = models.ForeignKey(Spanish, on_delete=models.CASCADE)

    def __str__(self):
        return self.text_clip

class ImageSpanish(models.Model):
    image_name = models.CharField(max_length=200)
    image_description = models.CharField(max_length=250)
    volume = models.ForeignKey(Spanish, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name