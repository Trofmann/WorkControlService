from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from works.forms import WorkModalForm
from works.models import Work, Subject
from works.views.base import BaseUpdateCreateView


class WorksListView(LoginRequiredMixin, ListView):
    """Работы по предмету"""
    title = 'Работы'
    context_object_name = 'works'
    template_name = 'works/works_list.html'

    def get_queryset(self):
        return Work.objects.filter(subject=self.subject)

    def get_context_data(self, **kwargs):
        kwargs['subject'] = self.subject
        return super(WorksListView, self).get_context_data(**kwargs)

    @property
    def subject(self):
        return Subject.objects.get(pk=self.kwargs['subject_pk'])

    @property
    def add_url(self):
        return reverse('works:add_work', args=[self.subject.pk])

    @property
    def update_url_str(self):
        return 'works:update_work'


class WorkUpdateCreateViewMixin(BaseUpdateCreateView):
    model = Work
    form_class = WorkModalForm

    entity_name = 'работа'
    entity_name_genitive = 'работы'
    entity_name_accusative = 'работу'

    @property
    def subject_pk(self):
        return self.kwargs.get('subject_pk') or self.object.subject.pk

    def get_success_url(self):
        return reverse('works:works_list', args=[self.subject_pk])

    def get_form_kwargs(self, **kwargs):
        kwargs = super(WorkUpdateCreateViewMixin, self).get_form_kwargs()
        kwargs['subject'] = Subject.objects.get(pk=self.subject_pk)
        return kwargs


class WorkCreateView(WorkUpdateCreateViewMixin, BSModalCreateView):
    """Создание работы"""
    pass


class WorkUpdateView(WorkUpdateCreateViewMixin, BSModalUpdateView):
    """Редактирование работы"""
    pass


@login_required
def delete_work(request, work_pk):
    """Удаление работы"""
    work = Work.objects.get(pk=work_pk)
    subject_pk = work.subject.pk
    work.delete()
    return HttpResponseRedirect(reverse('works:works_list', kwargs={'subject_pk': subject_pk}))
