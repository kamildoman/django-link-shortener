from django.db import models
from . import utils



class URLShortener(models.Model):
    url = models.CharField(max_length=500)
    shortened_url = models.CharField(max_length=30, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.shortened_url == None or self.shortened_url == "":
            self.shortened_url = utils.create_url(URLShortener)
        super(URLShortener, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
