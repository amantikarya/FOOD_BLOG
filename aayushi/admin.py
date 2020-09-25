from django.contrib import admin
from .models import Contact,  MYrecipie, Feedback

# Register your models here.
admin.site.register(Contact)
admin.site.register(MYrecipie)
admin.site.register(Feedback)