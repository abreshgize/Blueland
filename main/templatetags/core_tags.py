import os

from django import template
from django.conf import settings

register = template.Library()

# this is just to retreive the images by joining the servers path and z dynamic 
# image url
mp = '' if settings.DEBUG else 'https://bluelandmedical.com/blueland_media' 

@register.filter
def get_img(img):
    if img:
        return mp+img.url
    return ''


@register.simple_tag
def subtract(a, b):
    try:
        return a - b
    except:
        return 0