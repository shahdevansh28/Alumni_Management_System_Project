from multiprocessing import Event
from django.contrib import admin
from .models import User
from newApp.models import Events
from newApp.models import Demo

admin.site.register(User)
admin.site.register(Events)
admin.site.register(Demo)