from developer.models import (
    Company,
    CompanyContact,
    CompanyUser,
    DeveloperGroup,
    DeveloperPermission,
)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CompanyContactInline(admin.TabularInline):
    model = CompanyContact
    fields = ("type", "value")


class DeveloperPermissionInline(admin.TabularInline):
    model = CompanyUser.user_permissions.through


@admin.register(CompanyUser)
class CompanyUserAdmin(UserAdmin):
    inlines = (DeveloperPermissionInline,)
    readonly_fields = ("created_at", "update_at")
    list_display = ("username", "email", "phone", "is_active", "company")
    list_display_links = ("username",)
    fieldsets = (
        ("CompanyUser", {"fields": ("username", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "email",
                    "phone",
                    "avatar",
                    "country",
                    "company",
                    "created_at",
                    "update_at",
                ),
            },
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_banned", "is_superuser", "groups")},
        ),
    )
    add_fieldsets = (
        (
            "Creating new CompanyUser",
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "phone",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_filter = ("is_active",)
    search_fields = ("username", "email", "phone")
    ordering = ("username",)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = (CompanyContactInline,)
    list_display = (
        "id",
        "created_by",
        "title",
        "description",
        "email",
        "is_confirmed",
        "created_at",
        "is_active",
        "is_banned",
    )
    list_display_links = ("title",)
    search_fields = ("title",)
    ordering = ("title", "-created_at")


@admin.register(DeveloperPermission)
class DeveloperPermissionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "codename",
    )
    search_fields = ("name",)
    ordering = ("codename",)


@admin.register(DeveloperGroup)
class DeveloperGroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
