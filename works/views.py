from django.views.generic import ListView, CreateView

from works.forms import SubjectForm
from works.models import Work, Subject


class WorksListView(ListView):
    """Работы по предмету"""
    context_object_name = 'works'
    template_name = None

    def get_queryset(self):
        return Work.objects.filter(subject=self.kwargs['subject_pk'])


class SubjectsListView(ListView):
    """Все предметы"""
    context_object_name = 'subjects'
    template_name = 'works/index.html'

    def get_queryset(self):
        return Subject.objects.all()


class SubjectCreateView(CreateView):
    template_name = 'works/subject_form.html'
    form_class = SubjectForm
    success_url = '/'
