# Generated by Django 4.0.3 on 2022-05-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_alter_subject_name_alter_subject_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='work',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
    ]
