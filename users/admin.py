from django.contrib import admin
from .models import User, Car, WebApps

# Register your models here.
admin.site.register(User)
admin.site.register(WebApps)
admin.site.register(Car)
