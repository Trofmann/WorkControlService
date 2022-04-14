from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

from cabinet.models import ServiceUser


class UserCreationForm(BaseUserCreationForm):
    """Форма регистрации пользователя"""

    class Meta(BaseUserCreationForm.Meta):
        model = ServiceUser
