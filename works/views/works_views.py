from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from works.forms import WorkForm
from works.models import Work, Subject


class WorksListView(ListView):
    """Работы по предмету"""
    context_object_name = 'works'
    template_name = 'works/works_list.html'

    def get_queryset(self):
        return Work.objects.filter(subject=self.kwargs['subject_pk'])

    def get_context_data(self, **kwargs):
        kwargs['subject'] = Subject.objects.get(pk=self.kwargs['subject_pk'])
        return super(WorksListView, self).get_context_data(**kwargs)


class WorkCreateView(CreateView):
    template_name = 'works/form_base.html'
    form_class = WorkForm

    def get_success_url(self):
        return f'/{self.object.subject.pk}'

    def get_form_kwargs(self, **kwargs):
        kwargs = super(WorkCreateView, self).get_form_kwargs()
        kwargs['subject'] = Subject.objects.get(pk=self.kwargs.get('subject_pk'))
        return kwargs


def delete_work(request, work_pk):
    """Удаление работы"""
    work = Work.objects.get(pk=work_pk)
    subject_pk = work.subject.pk
    work.delete()
    return HttpResponseRedirect(reverse('works:works_list', kwargs={'subject_pk': subject_pk}))
