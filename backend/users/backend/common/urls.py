from common.views.v1.change_password_view import ChangePasswordAPIView
from common.views.v1.contacttype_view import ContactTypeViewSet
from common.views.v1.countrylist_view import CountryViewSet
from common.views.v1.get_jwt_view import GetJwtView
from common.views.v1.logout_view import JWTLogoutView
from common.views.v1.totp_view import CheckTOTPView
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"countries", CountryViewSet, basename="countries")
router.register(r"contact_types", ContactTypeViewSet, basename="contact_types")

urlpatterns = router.urls

generic_routs = [
    path("logout/", JWTLogoutView.as_view(), name="logout"),
    path("get-jwt/", GetJwtView.as_view(), name="get-jwt"),
    path("check-totp/", CheckTOTPView.as_view(), name="check-totp"),
    path("set-password/", CheckTOTPView.as_view(), name="totp-set-password"),
    path("change_passworg/", ChangePasswordAPIView.as_view(), name="user_change_password"),
]

urlpatterns += generic_routs
