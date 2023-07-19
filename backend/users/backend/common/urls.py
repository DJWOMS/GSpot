from common.views.v1.account_me_single_view import AccountSingleUserViewSet
from common.views.v1.account_me_view import AccountViewSet
from common.views.v1.account_multiple_view import AccountMultipleUsersViewSet
from common.views.v1.change_password_view import ChangePasswordAPIView
from common.views.v1.contacttype_view import ContactTypeViewSet
from common.views.v1.countrylist_view import CountryViewSet
from common.views.v1.logout_view import JWTLogoutView
from common.views.v1.token_refresh_view import GetJwtView
from common.views.v1.totp_view import CheckTOTPView
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"countries", CountryViewSet, basename="countries")
router.register(r"contact_types", ContactTypeViewSet, basename="contact_types")

urlpatterns = [
    path("logout/", JWTLogoutView.as_view(), name="logout"),
    path("common/", include(router.urls), name="common"),
    path("token_refresh/", GetJwtView.as_view(), name="token_refresh"),
    path("check-totp/", CheckTOTPView.as_view(), name="check-totp"),
    path("set-password/", CheckTOTPView.as_view(), name="totp-set-password"),
    path("change_passworg/", ChangePasswordAPIView.as_view(), name="user_change_password"),
]

account_router = [
    path(
        "account/me",
        AccountViewSet.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "destroy"},
        ),
        name="user-account",
    ),
    path(
        "account/me/<uuid:user_id>/",
        AccountSingleUserViewSet.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "delete"},
        ),
        name="user-single-account",
    ),
    path(
        "account/me",
        AccountMultipleUsersViewSet.as_view(
            {"post": "retrieve"},
        ),
        name="user-mixed-accounts",
    ),
]

urlpatterns += account_router
