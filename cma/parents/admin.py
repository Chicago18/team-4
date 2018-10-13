from django.contrib import admin
from . models import Register,Household
from django.utils.html import format_html
# from django.core.urlresolvers import reverse
# Register your models here.
admin.site.register(Register)
admin.site.register(Household)
