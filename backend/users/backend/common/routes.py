from rest_framework.routers import Route, DynamicRoute, SimpleRouter


class CustomChangeInfoAccountRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
    ]


class CustomChangePasswordRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={
                'get': 'retrieve',
                'patch': 'partial_update'
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
    ]