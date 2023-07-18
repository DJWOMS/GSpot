AVATAR_PATH = str


def get_avatar_upload_path(instance, filename: str) -> AVATAR_PATH:
    """
    :param instance: BaseAbstractUser
    Example: <class 'customer.models.CustomerUser'> or <class 'administrator.models.Admin'>
    Get the name of the module - this will be the desired folder
    :param filename: user avatar
    """

    user_type = instance._meta.app_label
    avatar_path = f'avatars/{user_type}/{filename}'
    return avatar_path
