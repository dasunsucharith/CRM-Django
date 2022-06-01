from django.contrib import admin

# Register your models here.

from .models import User, Deal, Agent, UserProfile 

admin.site.register(User)
admin.site.register(Deal)
admin.site.register(Agent)
admin.site.register(UserProfile)
