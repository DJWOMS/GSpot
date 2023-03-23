from django.contrib import admin

from .models import Language, ProductLanguage, Genre, SubGenre, SubgenreProduct


class GenreAdmin(admin.ModelAdmin):
    pass


class SubGenreAdmin(admin.ModelAdmin):
    pass


class LanguageAdmin(admin.ModelAdmin):
    pass


class ProductLanguageAdmin(admin.ModelAdmin):
    pass


class SubgenreProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Language, LanguageAdmin)
admin.site.register(ProductLanguage, ProductLanguageAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(SubGenre, SubGenreAdmin)
admin.site.register(SubgenreProduct, SubgenreProductAdmin)
