from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from admins.models import AdminPermission

User = get_user_model()


class AdminBackend(ModelBackend):
    """
    Authenticate Admin users by AdminPermission
    """

    def _get_group_permissions(self, user_obj):
<<<<<<< HEAD
        user_groups_field = User._meta.get_field("groups")
=======
        user_groups_field = get_user_model()._meta.get_field("groups")
>>>>>>> d90b3a48026019cca98123d3f6bf6b31681a890e
        user_groups_query = "group__%s" % user_groups_field.related_query_name()
        res = AdminPermission.objects.filter(**{user_groups_query: user_obj})
        return res
