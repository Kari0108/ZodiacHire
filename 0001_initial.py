# Generated by Django 5.1.3 on 2024-11-15 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
            ],
            options={
                'verbose_name': 'роль',
                'verbose_name_plural': 'роли',
                'db_table': 'roles',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
            ],
            options={
                'verbose_name': 'команда',
                'verbose_name_plural': 'команды',
                'db_table': 'teams',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('surname', models.CharField(max_length=100, verbose_name='фамилия')),
                ('patronymic', models.CharField(max_length=100, verbose_name='отчество')),
                ('date_of_birth', models.DateField(verbose_name='дата рождения')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
                ('team_compatibility', models.IntegerField(verbose_name='совместимость с командой')),
                ('company_compatibility', models.IntegerField(verbose_name='совместимость с компанией')),
                ('data_joined', models.DateField(auto_now_add=True, verbose_name='дата присоединения')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='astro_check.role', verbose_name='роль')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='astro_check.team', verbose_name='команда')),
            ],
            options={
                'verbose_name': 'работник',
                'verbose_name_plural': 'работники',
                'db_table': 'workers',
                'ordering': ['-data_joined', 'id'],
            },
        ),
    ]
