# Generated by Django 2.2 on 2020-05-06 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0003_auto_20200506_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='category',
            field=models.CharField(choices=[('CA', 'Carpenter'), ('PL', 'Plumber'), ('EL', 'Electrical Repairs'), ('AC', 'AC Repairs'), ('PA', 'Painters'), ('MC', 'Misc')], max_length=3),
        ),
    ]
