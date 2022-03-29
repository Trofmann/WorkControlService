from django.urls import re_path

from cabinet.views import LoginView, LogoutView

app_name = 'cabinet'

urlpatterns = [
    re_path('^login/', LoginView.as_view(), name='login'),
    re_path('^logout/', LogoutView.as_view(), name='logout'),
]
