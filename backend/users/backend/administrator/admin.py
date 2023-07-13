from administrator.models import (
    Admin,
    AdminGroup,
    AdminPermission,
    CompanyModerate,
    CompanyUserModerate,
    CustomerModerate,
)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class AdministratorPermissionInline(admin.TabularInline):
    model = Admin.user_permissions.through


@admin.register(AdminPermission)
class AdministratorPermissionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "codename",
    )
    list_display_links = ("name",)
    ordering = ("codename",)


@admin.register(AdminGroup)
class AdministratorGroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    ordering = ("name",)


@admin.register(Admin)
class CompanyUserAdmin(UserAdmin):
    inlines = (AdministratorPermissionInline,)
    readonly_fields = ("created_at", "update_at")
    list_display = ("username", "email", "phone", "is_active", "is_staff")
    list_display_links = ("username",)
    fieldsets = (
        ("Administrator", {"fields": ("username", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "email",
                    "phone",
                    "avatar",
                    "country",
                    "created_at",
                    "update_at",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_banned",
                    "is_superuser",
                    "is_staff",
                    "groups",
                    "developer_groups",
                    "developer_permissions",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            "Creating new Administrator",
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
    list_filter = ("username", "is_staff")
    search_fields = ("username", "email", "phone")
    ordering = ("username",)


@admin.register(CustomerModerate)
class CustomerModerateAdmin(admin.ModelAdmin):
    list_display = ("customer", "admin", "reason", "date", "action")
    ordering = ("date", "action")


@admin.register(CompanyUserModerate)
class CompanyUserModerateAdmin(admin.ModelAdmin):
    list_display = ("company_user", "admin", "reason", "date", "action")
    ordering = ("date", "action")


@admin.register(CompanyModerate)
class CompanyModerateAdmin(admin.ModelAdmin):
    list_display = ("company", "admin", "reason", "date", "action")
    ordering = ("date", "action")
