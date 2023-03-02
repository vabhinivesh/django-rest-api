from django.contrib import admin
from base.models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(TaskStatus)
admin.site.register(Task)
