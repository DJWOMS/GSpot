from django.urls import path, include
from rest_framework import routers

from common.views.v1.contacttype_view import ContactTypeViewSet
from common.views.v1.countrylist_view import CountryViewSet
from common.views.v1.logout_view import JWTLogoutView
from common.views.v1.get_jwt_view import GetJwtView
<<<<<<< HEAD
from common.views.v1.totp_view import CheckTOTPView
=======
from common.views.v1.change_password_view import ChangePasswordAPIView
>>>>>>> 6ef0f6f (* change detail changepassword to general method in common)

router = routers.DefaultRouter()
router.register(r"countries", CountryViewSet, basename="countries")
router.register(r"contact_types", ContactTypeViewSet, basename="contact_types")

urlpatterns = router.urls

generic_routs = [
    path("logout/", JWTLogoutView.as_view(), name="logout"),
    path("get-jwt/", GetJwtView.as_view(), name="get-jwt"),
<<<<<<< HEAD
    path("check-totp/", CheckTOTPView.as_view(), name="check-totp"),
    path("set-password/", CheckTOTPView.as_view(), name="totp-set-password"),
=======
    path("change_passworg/", ChangePasswordAPIView.as_view(), name="user_change_password"),
>>>>>>> 6ef0f6f (* change detail changepassword to general method in common)
]

urlpatterns += generic_routs
