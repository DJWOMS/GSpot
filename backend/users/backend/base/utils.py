AVATAR_PATH = str


def avatar_upload_path(instance, filename: str) -> AVATAR_PATH:
    """
    :param instance: BaseAbstractUser
    Example: <class 'customer.models.CustomerUser'> or <class 'administrator.models.Admin'>
    Get the name of the module - this will be the desired folder

    - media
        - customers
            - avatar.png
        - administrators
            - photo.jpg
        - developers
            - image.png
            ...

    :param filename: user avatar
    """

    user_type = f'{type(instance)}'.split("'")[1].split(".")[0]
    avatar_path = f'{user_type}s/{filename}'
    return avatar_path
