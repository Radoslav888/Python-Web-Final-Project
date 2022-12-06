from django.conf.urls.static import static
from django.urls import path, include

from Hestia import settings
from Hestia.accounts.views import SignInView, SignUpView, SignOutView, EditUserView, UserDeleteView, \
    user_details_view

urlpatterns = [
    path('login/', SignInView.as_view(), name='log in'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', SignOutView.as_view(), name='log out'),
    path('profile/<int:pk>/', include([
        path('', user_details_view, name='details user'),
        path('edit/', EditUserView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)