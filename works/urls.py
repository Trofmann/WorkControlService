from django.urls import re_path

from works.views import SubjectsListView, WorksListView, SubjectCreateView, WorkCreateView, delete_subject, delete_work

app_name = 'works'

urlpatterns = []

# Предметы
urlpatterns += [
    re_path('^$', SubjectsListView.as_view(), name='subjects_list'),
    re_path('^add_subject/$', SubjectCreateView.as_view(), name='add_subject'),
    re_path('^delete_subject/(?P<subject_pk>[0-9]*)', delete_subject, name='delete_subject')
]

# Работы
urlpatterns += [
    re_path('^(?P<subject_pk>[0-9]*)/$', WorksListView.as_view(), name='works_list'),
    re_path('^add_work/(?P<subject_pk>[0-9]*)', WorkCreateView.as_view(), name='add_work'),
    re_path('^delete_work/(?P<work_pk>[0-9]*)', delete_work, name='delete_work')
]
