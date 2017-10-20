from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


from .validators import validate_url
from .utils import short_generator, create_shortcode

# Create your models here.

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class ShortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(ShortURLManager, self).all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs

    def refresh_shortcodes(self):
        qs = ShortURL.objects.filter(id__gte=1)
        new_codes=0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes +=1
        return "New codes made: {i}".format(i=new_codes)


class ShortURL(models.Model):
    url         = models.CharField(max_length=220, validators =[validate_url] )
    shortcode   = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    active      = models.BooleanField(default=True)

    objects = ShortURLManager()

    def get_short_url(self):
        url_path= reverse("shorturl", kwargs={shortcode:self.shortcode})
        return "http://www.doingandlearning.com/" + url_path

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode =="":
            self.shortcode = create_shortcode(self)
        super(ShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

