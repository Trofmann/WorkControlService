from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from works.forms import SubjectModalForm
from works.models import Subject
from works.views.base import BaseUpdateCreateView


class SubjectsListView(LoginRequiredMixin, ListView):
    """Все предметы"""
    title = 'Предметы'
    context_object_name = 'subjects'
    template_name = 'works/subjects_list.html'

    def get_queryset(self):
        return Subject.objects.filter(user=self.request.user)

    @property
    def add_url_str(self):
        return 'works:add_subject'

    @property
    def update_url_str(self):
        return 'works:update_subject'


class SubjectCreateUpdateViewMixin(BaseUpdateCreateView):
    template_name = 'modal.html'
    form_class = SubjectModalForm
    model = Subject

    entity_name = 'предмет'
    entity_name_genitive = 'предмета'
    entity_name_accusative = 'предмет'

    def get_success_url(self):
        return reverse('works:subjects_list')

    def get_form_kwargs(self, **kwargs):
        kwargs = super(SubjectCreateUpdateViewMixin, self).get_form_kwargs(**kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class SubjectCreateModalView(SubjectCreateUpdateViewMixin, BSModalCreateView):
    pass


class SubjectUpdateModalView(SubjectCreateUpdateViewMixin, BSModalUpdateView):
    pass


@login_required
def delete_subject(request, subject_pk):
    """Удаление предмета"""
    Subject.objects.get(pk=subject_pk).delete()
    return HttpResponseRedirect(reverse('works:subjects_list'))
