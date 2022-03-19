import datetime

from django.db import models

from works.consts import STATUSES, NOT_STARTED_CODE


class Subject(models.Model):
    """Предмет"""
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        null=False, blank=False,
        unique=True,
    )

    class Meta:
        verbose_name = 'Предмет',
        verbose_name_plural = 'Предметы'
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def works_count(self):
        """Количество работ по предмету"""
        return models.Count(self.works)


class Work(models.Model):
    """Работа"""
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        null=False, blank=False,
    )

    subject = models.ForeignKey(
        to=Subject,
        verbose_name='Предмет',
        related_name='works',
        on_delete=models.CASCADE,
        null=False, blank=False,
    )

    deadline = models.DateField(
        verbose_name='Дата выполнения',
        null=True, blank=True,
    )

    status = models.IntegerField(
        verbose_name='Статус',
        null=False, blank=False,
        choices=STATUSES,
        default=NOT_STARTED_CODE,
    )

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
        ordering = ['deadline', 'status', 'name']

    def __str__(self):
        return self.name

    @property
    def expired(self):
        return datetime.datetime.now() > self.deadline
