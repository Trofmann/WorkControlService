from django.contrib.auth.models import AbstractUser


class ServiceUser(AbstractUser):
    """
    Кастомная модель пользователя

    Создана на случай возможного расширения базовой модели
    """
    pass
