from django import forms
from django.forms import SelectDateWidget

from works.models import Subject, Work
from bootstrap_modal_forms.forms import BSModalModelForm


class SubjectForm(forms.ModelForm):
    """Форма добавления предмета"""

    class Meta:
        model = Subject
        fields = (
            'name',
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(SubjectForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.user = self.user
        return super(SubjectForm, self).save(commit)


class SubjectModalForm(BSModalModelForm):
    """Форма добавления предмета"""

    class Meta:
        model = Subject
        fields = (
            'name',
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(SubjectModalForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.user = self.user
        return super(SubjectModalForm, self).save(commit)


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
