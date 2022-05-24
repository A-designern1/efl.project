from django.contrib import admin
from .models import User, League, Team

admin.site.register(User),
admin.site.register(League),
admin.site.register(Team)

# Register your models here.
