from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.views.generic import TemplateView


class TitleView(TemplateView):
    """Главная страница"""
    template_name = 'cabinet/title_page.html'


class LoginView(BaseLoginView):
    """Вход на сайт"""
    template_name = 'cabinet/login.html'


class LogoutView(BaseLogoutView):
    """Выход с сайта"""
    pass
