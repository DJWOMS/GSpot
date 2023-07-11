from developer.models import (
    Company,
    CompanyContact,
    CompanyUser,
    DeveloperGroup,
    DeveloperPermission,
)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


##############################
# INLINES
##############################
class CompanyContactInline(admin.TabularInline):
    model = CompanyContact
    fields = ("type", "value")


class DeveloperPermissionInline(admin.TabularInline):
    model = DeveloperPermission
    fields = ("name", "codename")


##############################
# MODELS
##############################
@admin.register(CompanyUser)
class CompanyUserAdmin(UserAdmin):
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
            {"fields": ("is_active", "is_banned", "is_superuser", "groups", "user_permissions")},
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
    # readonly_fields = ("user_permissions",)
    # filter_horizontal = ("groups", "users_permissions")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = (CompanyContactInline,)
    list_display = (
        "id",
        "created_by",
        "title",
        "description",
        "email",
        "image",
        "is_confirmed",
        "created_at",
        "is_active",
        "is_banned",
    )
    ordering = ("title", "-created_at")


@admin.register(DeveloperPermission)
class DeveloperPermissionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "codename",
    )
    ordering = ("codename",)


# admin.site.register(DeveloperGroup)


@admin.register(DeveloperGroup)
class DeveloperGroupAdmin(admin.ModelAdmin):
    def get_permission(self, obj: DeveloperGroup):
        return ", ".join([permission.name for permission in obj.permission.all()])

    get_permission.short_description = "Permision Name"

    list_display = (
        "name",
        "get_permission",
    )
    ordering = ("name",)
