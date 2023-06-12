from django.contrib import admin
from .models import UserProfile, HappyDay, Message

admin.site.register(UserProfile)

admin.site.register(HappyDay)

admin.site.register(Message)