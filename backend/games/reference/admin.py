from django.contrib import admin
from models import *

class GanreAdmin(admin.ModelAdmin):
    class Meta():
        madels = Ganre
        
class SubGanreAdmin (admin.ModelAdmin):
    class Meta():
        models = SubGanre
        
admin.site.register(Ganre, GanreAdmin)
admin.site.register(SubGanre, SubGanreAdmin)