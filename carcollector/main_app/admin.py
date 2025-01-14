from django.contrib import admin
from .models import Car
from .models import Oil
from .models import Medal
# Register your models here.

admin.site.register(Car)
admin.site.register(Oil)
admin.site.register(Medal)
