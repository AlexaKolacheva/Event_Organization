from django.contrib import admin

from apps.events.models import CustomUser, Category, Event, Comments, Participation


admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Comments)
admin.site.register(Participation)

# Register your models here.
