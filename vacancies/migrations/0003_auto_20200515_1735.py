# Generated by Django 3.0.6 on 2020-05-15 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_auto_20200515_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name'], 'verbose_name': 'компания', 'verbose_name_plural': 'компании'},
        ),
        migrations.AlterModelOptions(
            name='specialty',
            options={'ordering': ['title'], 'verbose_name': 'специализация', 'verbose_name_plural': 'специализации'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['title'], 'verbose_name': 'вакансия', 'verbose_name_plural': 'вакансии'},
        ),
    ]
