from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from works.forms import SubjectForm
from works.models import Subject


class SubjectsListView(ListView):
    """Все предметы"""
    context_object_name = 'subjects'
    template_name = 'works/subjects_list.html'

    def get_queryset(self):
        return Subject.objects.all()


class SubjectCreateUpdateViewMixin(object):
    model = Subject
    template_name = 'works/form_base.html'
    form_class = SubjectForm
    success_url = '/'


class SubjectCreateView(SubjectCreateUpdateViewMixin, CreateView):
    pass


class SubjectUpdateView(SubjectCreateUpdateViewMixin, UpdateView):
    pass


def delete_subject(request, subject_pk):
    """Удаление предмета"""
    Subject.objects.get(pk=subject_pk).delete()
    return HttpResponseRedirect(reverse('works:subjects_list'))
