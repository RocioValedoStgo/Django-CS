# Generated by Django 2.2.1 on 2019-06-03 08:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('yearsExperience', models.IntegerField()),
                ('phoneNumber', models.IntegerField()),
                ('birthday', models.DateField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Profesor',
            },
        ),
    ]
