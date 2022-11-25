from django.urls import path

from Hestia.accounts.views import SignInView, SignUpView, SignOutView

urlpatterns = [
    path('login/', SignInView.as_view(), name='log in'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', SignOutView.as_view(), name='log out'),
]