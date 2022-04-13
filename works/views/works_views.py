from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from works.forms import WorkForm
from works.models import Work, Subject


class WorksListView(LoginRequiredMixin, ListView):
    """Работы по предмету"""
    context_object_name = 'works'
    template_name = 'works/works_list.html'

    def get_queryset(self):
        return Work.objects.filter(subject=self.kwargs['subject_pk'])

    def get_context_data(self, **kwargs):
        kwargs['subject'] = Subject.objects.get(pk=self.kwargs['subject_pk'])
        return super(WorksListView, self).get_context_data(**kwargs)


class WorkUpdateCreateViewMixin(LoginRequiredMixin):
    model = Work
    template_name = 'works/form_base.html'
    form_class = WorkForm

    def get_success_url(self):
        return reverse('works:works_list', args=[self.object.subject.pk])


class WorkCreateView(WorkUpdateCreateViewMixin, CreateView):
    """Создание работы"""

    def get_form_kwargs(self, **kwargs):
        kwargs = super(WorkCreateView, self).get_form_kwargs()
        kwargs['subject'] = Subject.objects.get(pk=self.kwargs.get('subject_pk'))
        return kwargs


class WorkUpdateView(WorkUpdateCreateViewMixin, UpdateView):
    """Редактирование работы"""

    def get_form_kwargs(self, **kwargs):
        kwargs = super(WorkUpdateView, self).get_form_kwargs()
        kwargs['subject'] = Subject.objects.get(pk=self.object.subject.pk)
        return kwargs


@login_required
def delete_work(request, work_pk):
    """Удаление работы"""
    work = Work.objects.get(pk=work_pk)
    subject_pk = work.subject.pk
    work.delete()
    return HttpResponseRedirect(reverse('works:works_list', kwargs={'subject_pk': subject_pk}))
