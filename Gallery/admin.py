# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Images,Location,Category
# Register your models here.
admin.site.register(Images)
admin.site.register(Location)
admin.site.register(Category)
