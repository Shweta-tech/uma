# Generated by Django 2.0 on 2020-06-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childreg',
            name='bd',
        ),
        migrations.AddField(
            model_name='childreg',
            name='birth_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
