# Generated by Django 3.2.16 on 2022-12-10 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-04-23'),
            preserve_default=False,
        ),
    ]
