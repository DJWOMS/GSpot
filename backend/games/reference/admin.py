from django.contrib import admin

from . import models


class LanguageAdmin(admin.ModelAdmin):
    pass


class ProductLanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.ProductLanguage, ProductLanguageAdmin)
