# Generated by Django 2.2 on 2020-04-29 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('CA', 'Carpenter'), ('PL', 'Plumber'), ('EL', 'Electrical Repairs'), ('AC', 'AC Repairs'), ('PA', 'Painters')], max_length=3)),
                ('slug', models.SlugField()),
                ('task', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('handyman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Advertisment',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nameSlug', models.SlugField(unique=True)),
                ('price', models.FloatField()),
            ],
            options={
                'db_table': 'Service',
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('appointment_date', models.DateTimeField(blank=True, null=True)),
                ('durations', models.TimeField(blank=True, null=True)),
                ('completion_date', models.DateTimeField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('advertisment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapp.Advertisment')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
                ('handyman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handyman', to=settings.AUTH_USER_MODEL)),
                ('services', models.ManyToManyField(to='mapp.Service')),
            ],
            options={
                'db_table': 'Assignment',
                'ordering': ['appointment_date'],
            },
        ),
        migrations.AddField(
            model_name='advertisment',
            name='services',
            field=models.ManyToManyField(to='mapp.Service'),
        ),
    ]
