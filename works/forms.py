from django import forms

from works.models import Subject, Work


class SubjectForm(forms.ModelForm):
    """Форма добавления предмета"""

    class Meta:
        model = Subject
        fields = '__all__'


class WorkForm(forms.ModelForm):
    """Форма добавления """

    class Meta:
        model = Work
        fields = '__all__'
