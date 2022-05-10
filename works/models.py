import datetime

from django.db import models

from cabinet.models import ServiceUser
from works.consts import STATUSES, NOT_STARTED_CODE, STATUSES_DICT, IN_WORK_CODE, COMPLETED_CODE


class Subject(models.Model):
    """Предмет"""
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        null=False, blank=False,
        unique=False,
    )

    user = models.ForeignKey(
        to=ServiceUser,
        verbose_name='Пользователь',
        related_name='subjects',
        on_delete=models.CASCADE,
        null=False, blank=False,
    )

    comment = models.TextField(
        verbose_name='Комментарий',
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Предмет',
        verbose_name_plural = 'Предметы'
        ordering = ['name']
        unique_together = ['name', 'user']

    def __str__(self):
        return self.name

    @property
    def not_started_works_count(self):
        """Количество работ в статусе 'Не начато'"""
        return self.works.filter(status=NOT_STARTED_CODE).count()

    @property
    def in_work_works_count(self):
        """Количество работ в статусе 'В работе'"""
        return self.works.filter(status=IN_WORK_CODE).count()

    @property
    def completed_works_count(self):
        """Количество работ в статусе 'Выполнено'"""
        return self.works.filter(status=COMPLETED_CODE).count()

    @property
    def expired_works_count(self):
        """Количество просроченных работ"""
        count_ = 0
        for work in self.works.all():
            count_ += work.expired
        return count_

    @property
    def total_works_count(self):
        """Количество работ по предмету"""
        return self.works.count()

    @property
    def completed(self):
        """Выполнены все работы по предмету"""
        return self.total_works_count == self.completed_works_count

    @property
    def has_expired(self):
        """Есть просроченные работы по предмету"""
        return bool(self.expired_works_count)


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

    comment = models.TextField(
        verbose_name='Комментарий',
        null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
        ordering = ['deadline', 'status', 'name']

    def __str__(self):
        return self.name

    @property
    def status_str(self):
        """Статус хранится в виде числа, а отображать надо в виде слова"""
        return STATUSES_DICT[self.status]

    @property
    def expired(self):
        if self.deadline is not None:
            today = datetime.datetime.today()
            today_date = datetime.date(year=today.year, month=today.month, day=today.day)
            return (self.status != COMPLETED_CODE) and (today_date > self.deadline)
        return False

    @property
    def deadline_table_value(self):
        return self.deadline if self.deadline is not None else '—'

    @property
    def completed(self):
        return self.status == COMPLETED_CODE
