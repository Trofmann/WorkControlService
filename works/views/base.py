from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView


class BaseUpdateCreateView(LoginRequiredMixin):
    """Базовый миксин для создания и редактирования записей"""
    template_name = 'form_base.html'

    create_action = 'Добавление'
    update_action = 'Редактирование'

    @property
    def action(self):
        if isinstance(self, CreateView):
            return self.create_action
        return self.update_action

    @property
    def title(self):
        return f'{self.action} {self.entity_name_genitive}'
