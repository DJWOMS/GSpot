from common.models import ContactType, Country
from django.contrib import admin
from django.contrib.admin import TabularInline
from django.urls import reverse
from django.utils.html import format_html


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(ContactType)
class ContactTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "icon")
