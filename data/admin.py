# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Private libraries
from .models import gallery, image, location, acceleration, temperature, humidity

# Register your models here.
admin.site.register(location)
admin.site.register(acceleration)
admin.site.register(temperature)
admin.site.register(humidity)
admin.site.register(image)
admin.site.register(gallery)