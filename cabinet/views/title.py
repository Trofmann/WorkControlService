from django.views.generic import TemplateView


class TitleView(TemplateView):
    """Главная страница"""
    template_name = 'cabinet/title_page.html'
