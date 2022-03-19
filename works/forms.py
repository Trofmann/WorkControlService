from django import forms

from works.models import Subject


class SubjectForm(forms.ModelForm):
    """Форма добавления предмета"""

    class Meta:
        model = Subject
        fields = '__all__'
