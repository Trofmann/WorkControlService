from django.urls import re_path

from works.views import SubjectsListView, WorksListView, SubjectCreateView, WorkCreateView

app_name = 'works'
urlpatterns = [
    re_path('^$', SubjectsListView.as_view(), name='index'),
    re_path('^(?P<subject_pk>[0-9]*)/$', WorksListView.as_view(), name='works_list'),
    re_path('^add_subject/$', SubjectCreateView.as_view(), name='add_subject'),
    re_path('^add_work/(?P<subject_pk>[0-9]*)', WorkCreateView.as_view(), name='add_work'),
]
