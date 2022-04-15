from django.urls import reverse
from django.views.generic import CreateView

from cabinet.forms import UserCreationForm


class RegistrationView(CreateView):
    """Регистрация пользователя"""
    title = 'Регистрация'
    form_class = UserCreationForm
    template_name = 'form_base.html'

    def get_success_url(self):
        return reverse('works:subjects_list')