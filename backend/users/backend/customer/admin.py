from customer.models import CustomerUser, FriendShipRequest
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class FriendInline(admin.TabularInline):
    model = CustomerUser.friends.through
    fk_name = "sender"


@admin.register(CustomerUser)
class CustomerAdmin(UserAdmin):
    def get_friends(self, obj):
        return ", ".join([friend.username for friend in obj.friends.all()])

    get_friends.short_description = "Friends"

    readonly_fields = ("get_friends", "age", "created_at", "update_at")
    fieldsets = (
        ("Customer", {"fields": ("username", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "email",
                    "phone",
                    "birthday",
                    "avatar",
                    "country",
                    "age",
                    "created_at",
                    "update_at",
                ),
            },
        ),
        ("Additional Info", {"fields": ("is_active",)}),
        ("Friends List", {"fields": ("get_friends",)}),
    )
    add_fieldsets = (
        (
            "Creating new customer",
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "phone",
                    "password1",
                    "password2",
                    "birthday",
                    "is_active",
                ),
            },
        ),
    )
    list_display = ("username", "email", "phone", "birthday", "is_active")
    list_display_links = ("username",)
    list_filter = ("is_active",)
    search_fields = ("username", "email", "phone")
    ordering = ("username",)
    filter_horizontal = ()
    inlines = (FriendInline,)
