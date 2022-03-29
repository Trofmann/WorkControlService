from django import forms
from django.forms import SelectDateWidget

from works.models import Subject, Work


class SubjectForm(forms.ModelForm):
    """Форма добавления предмета"""

    class Meta:
        model = Subject
        fields = '__all__'


class WorkForm(forms.ModelForm):
    """Форма добавления работы"""
    deadline = forms.DateField(
        label='Дедлайн',
        required=False,
        widget=SelectDateWidget
    )

    class Meta:
        model = Work
        exclude = (
            'subject',
        )

    def __init__(self, subject, **kwargs):
        self.subject = subject
        super(WorkForm, self).__init__(**kwargs)

    def save(self, commit=True):
        self.instance.subject = self.subject
        return super(WorkForm, self).save(commit)
