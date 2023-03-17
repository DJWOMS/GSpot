from django.contrib import admin

from .models import Language, ProductLanguage


class LanguageAdmin(admin.ModelAdmin):
    pass


class ProductLanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Language, LanguageAdmin)
admin.site.register(ProductLanguage, ProductLanguageAdmin)
