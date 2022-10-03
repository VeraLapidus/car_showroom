# Generated by Django 4.1.1 on 2022-10-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя покупателя')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия покупателя')),
                ('year_of_birth', models.IntegerField(blank=True, verbose_name='Год рождения')),
                ('balance', models.IntegerField(default=0, verbose_name='Баланс покупателя, USD')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'ФИ покупателя',
                'verbose_name_plural': 'ФИ покупателей',
            },
        ),
    ]
