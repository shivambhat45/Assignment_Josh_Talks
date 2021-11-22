from django.contrib import admin
from AppApi import models

# Register your models here.
admin.site.register(models.VideoInfo)

# For Accessing the models from the admin panel you need to register those models here