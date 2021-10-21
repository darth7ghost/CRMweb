from re import A
from django.contrib import admin
from .models import User, Lead, Agent, userProfile

# Register your models here.
admin.site.register(User)
admin.site.register(userProfile)
admin.site.register(Lead)
admin.site.register(Agent)