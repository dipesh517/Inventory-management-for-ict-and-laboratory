from django.contrib import admin
from .models import Room
from .models import Computer
from .models import Laptop
from .models import NetworkSwitch
from .models import Printer
from .models import AdditionalItem

# Register your models here.


admin.site.register(Room)
admin.site.register(Computer)
admin.site.register(Laptop)
admin.site.register(NetworkSwitch)
admin.site.register(Printer)
admin.site.register(AdditionalItem)

