

from django.urls import path, include

from Hestia.accounts.views import SignInView, SignUpView, SignOutView, UserDetailsView, EditUserView, UserDeleteView

urlpatterns = [
    path('login/', SignInView.as_view(), name='log in'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', SignOutView.as_view(), name='log out'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', EditUserView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
]