from django.urls import re_path

from works.views import SubjectsListView, WorksListView, SubjectCreateView

app_name = 'works'
urlpatterns = [
    re_path('^$', SubjectsListView.as_view(), name='index'),
    re_path('^(?P<subject_id>[0-9]*)/$', WorksListView.as_view(), name='works'),
    re_path('^add_subject/$', SubjectCreateView.as_view(), name='add_subject'),
]
