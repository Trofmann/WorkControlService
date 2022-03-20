from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from works.forms import SubjectForm
from works.models import Subject


class SubjectsListView(ListView):
    """Все предметы"""
    context_object_name = 'subjects'
    template_name = 'works/subjects_list.html'

    def get_queryset(self):
        return Subject.objects.all()


class SubjectCreateView(CreateView):
    template_name = 'works/form_base.html'
    form_class = SubjectForm
    success_url = '/'


def delete_subject(request, subject_pk):
    """Удаление предмета"""
    Subject.objects.get(pk=subject_pk).delete()
    return HttpResponseRedirect(reverse('works:subjects_list'))
