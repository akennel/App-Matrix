from django.contrib import admin

from .models import Server
from .models import Service
from .models import Skill
from .models import App

admin.site.register(Service)
admin.site.register(Skill)
admin.site.register(App)
admin.site.register(Server)