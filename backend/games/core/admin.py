from django.contrib import admin

from .models import Product, GameDlcLink, SystemRequirement


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass

class GameDlcLinkAdmin(admin.ModelAdmin):
    pass

class SystemRequirementAdmin(admin.ModelAdmin):
    pass

# при регистрации модели Post источником конфигурации
# для неё назначаем класс PostAdmin
admin.site.register(Product, ProductAdmin)
admin.site.register(GameDlcLink, GameDlcLinkAdmin)
admin.site.register(SystemRequirement, SystemRequirementAdmin)
