from django.contrib import admin
from .models import models
from .models import Task


# Register your models here.
from . import *
admin.site.register(Task)

