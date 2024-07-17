# UserCreationForm -> Signup
# UserChangeForm -> Admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'age', 'email')


class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'age', 'email')
