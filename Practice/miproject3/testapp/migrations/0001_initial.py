# Generated by Django 4.1.5 on 2023-09-09 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.person')),
                ('eno', models.IntegerField()),
                ('salary', models.FloatField()),
            ],
            options={
                'db_table': 'employee',
            },
            bases=('testapp.person',),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.employee')),
                ('exp', models.IntegerField()),
                ('team_size', models.IntegerField()),
            ],
            options={
                'db_table': 'manager',
            },
            bases=('testapp.employee',),
        ),
    ]
