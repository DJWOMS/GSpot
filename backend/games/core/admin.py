from django.contrib import admin

from . import models


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass


class GameDlcLinkAdmin(admin.ModelAdmin):
    pass


class SystemRequirementAdmin(admin.ModelAdmin):
    pass


# при регистрации модели Product источником конфигурации
# для неё назначаем класс ProductAdmin
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.GameDlcLink, GameDlcLinkAdmin)
admin.site.register(models.SystemRequirement, SystemRequirementAdmin)
