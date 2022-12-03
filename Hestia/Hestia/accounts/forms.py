from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UsernameField, UserCreationForm

UserModel = get_user_model()


class UserEditForm(UserChangeForm):

    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {
            'username': UsernameField,
        }


class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'phone_number')
        field_classes = {
            'username': UsernameField,
            }
