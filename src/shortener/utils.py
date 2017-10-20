from django.conf import settings
import random
import string

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)


def short_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = short_generator(size)
    Klass = instance.__class__
    if Klass.objects.filter(shortcode=new_code) is None:
        return create_shortcode(instance, size)
    return new_code