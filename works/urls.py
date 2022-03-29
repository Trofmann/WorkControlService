from django.urls import re_path

from works import views

app_name = 'works'

urlpatterns = []

# Предметы
urlpatterns += [
    re_path('^$', views.SubjectsListView.as_view(), name='subjects_list'),
    re_path('^add_subject/$', views.SubjectCreateView.as_view(), name='add_subject'),
    re_path('^update_subject/(?P<pk>[0-9]*)/$', views.SubjectUpdateView.as_view(), name='update_subject'),
    re_path('^delete_subject/(?P<subject_pk>[0-9]*)', views.delete_subject, name='delete_subject')
]

# Работы
urlpatterns += [
    re_path('^(?P<subject_pk>[0-9]*)/$', views.WorksListView.as_view(), name='works_list'),
    re_path('^add_work/(?P<subject_pk>[0-9]*)', views.WorkCreateView.as_view(), name='add_work'),
    re_path('^update_work/(?P<pk>[0-9]*)/$', views.WorkUpdateView.as_view(), name='update_work'),
    re_path('^delete_work/(?P<work_pk>[0-9]*)', views.delete_work, name='delete_work')
]
