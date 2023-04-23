def get_dict_of_user_permissions(user):
    permissions = {}
    user_permissions = user.user_permissions.all()
    if user_permissions:
        for permission in user_permissions:
            service_name = permission.content_type.service_name
            app_label = permission.content_type.app_label
            model = permission.content_type.model
            if service_name in permissions:
                if app_label in permissions[service_name]:
                    if model in permissions[service_name][app_label]:
                        permissions[service_name][app_label][model].append(permission.name)
                    else:
                        permissions[service_name][app_label][model] = [permission.name]
                else:
                    permissions[service_name][app_label] = {model: [permission.name]}
            else:
                permissions[service_name] = {app_label: {model: [permission.name]}}
    return permissions