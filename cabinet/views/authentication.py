from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView


class LoginView(BaseLoginView):
    """Вход на сайт"""
    title = 'Вход'
    template_name = 'cabinet/login.html'


class LogoutView(BaseLogoutView):
    """Выход с сайта"""
    pass
