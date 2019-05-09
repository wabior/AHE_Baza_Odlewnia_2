from django.contrib import admin
from .models import Project,Type,Forms,Machine,Production,User

# Register your models here.

admin.site.register(Project)
admin.site.register(Type)
admin.site.register(Forms)
admin.site.register(Machine)
admin.site.register(Production)
admin.site.register(User)

