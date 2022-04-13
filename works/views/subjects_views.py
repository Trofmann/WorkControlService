from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from works.forms import SubjectForm
from works.models import Subject


class SubjectsListView(LoginRequiredMixin, ListView):
    """Все предметы"""
    context_object_name = 'subjects'
    template_name = 'works/subjects_list.html'

    def get_queryset(self):
        return Subject.objects.filter(user=self.request.user)


class SubjectCreateUpdateViewMixin(LoginRequiredMixin):
    model = Subject
    template_name = 'works/form_base.html'
    form_class = SubjectForm

    def get_success_url(self):
        return reverse('works:subjects_list')

    def get_form_kwargs(self, **kwargs):
        kwargs = super(SubjectCreateUpdateViewMixin, self).get_form_kwargs(**kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class SubjectCreateView(SubjectCreateUpdateViewMixin, CreateView):
    pass


class SubjectUpdateView(SubjectCreateUpdateViewMixin, UpdateView):
    pass


@login_required
def delete_subject(request, subject_pk):
    """Удаление предмета"""
    Subject.objects.get(pk=subject_pk).delete()
    return HttpResponseRedirect(reverse('works:subjects_list'))
