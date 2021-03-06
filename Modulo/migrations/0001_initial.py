# Generated by Django 2.2.1 on 2019-06-10 20:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_esp32', models.IntegerField()),
                ('mac_esp32', models.CharField(max_length=100)),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.DateTimeField(blank=True, default=None, null=True)),
                ('idUser', models.ForeignKey(on_delete=models.SET(-1), to='User.User')),
            ],
            options={
                'db_table': 'Modulo',
            },
        ),
    ]
