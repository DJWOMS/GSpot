from django.urls import path
from customer.views.v1.auth_view import CustomerAuthView
from customer.views.v1 import account_views
from customer.views.v1.customer_registration_view import CustomerRegistrationView
from customer.views.v1 import customer_friend_view


urlpatterns = [
    path("registration/", CustomerRegistrationView.as_view()),
]

account_router = [
    path(
        "customer/me",
        account_views.AccountViewSet.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "destroy"}
        ),
        name="customer-user-account",
    ),
    path(
        "customer/me/change-password",
        account_views.ChangePasswordViewSet.as_view({"post": "create"}),
        name="customer-user-change-password",
    ),
]

auth_routes = [path("login/", CustomerAuthView.as_view(), name="customer_login")]

friends = [
    path('customers/', customer_friend_view.GetUsersList.as_view(), name='users-list'),
    path(
        'customers/<uuid:user_id>/',
        customer_friend_view.GetUserRetrieve.as_view(),
        name='user-retrieve',
    ),
    path(
        'customer/<uuid:user_id>/add-friend/',
        customer_friend_view.AddFriendsView.as_view(),
        name='add-friend',
    ),
    path(
        'friends_requests/',
        customer_friend_view.GetListAcceptAddFriendsView.as_view(),
        name='list-friends-requests',
    ),
    path(
        'friends_requests/<uuid:user_id>/ ',
        customer_friend_view.RetrieveAcceptRejectAddFriendsView.as_view(
            {'get': 'retrieve', 'post': 'create', 'delete': 'destroy'}
        ),
        name='retrieve-accept-reject-friend',
    ),
    path(
        'friends/',
        customer_friend_view.GetAllFriendsView.as_view(),
        name='my-friends',
    ),
    path(
        'friends/<uuid:user_id>/',
        customer_friend_view.RetrieveDestroyFriendsView.as_view(),
        name='retrieve-destroy-friend',
    ),
]

urlpatterns += account_router
urlpatterns += auth_routes
urlpatterns += friends
