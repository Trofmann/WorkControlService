from django.views.generic import ListView, CreateView

from works.forms import SubjectForm, WorkForm
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
    success_url = '/'


class SubjectsListView(ListView):
    """Все предметы"""
    context_object_name = 'subjects'
    template_name = 'works/index.html'

    def get_queryset(self):
        return Subject.objects.all()


class SubjectCreateView(CreateView):
    template_name = 'works/form_base.html'
    form_class = SubjectForm
    success_url = '/'
