# Generated by Django 2.2.9 on 2020-01-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200114_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banner_subtitle',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
