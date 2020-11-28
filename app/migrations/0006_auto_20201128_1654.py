# Generated by Django 3.1.1 on 2020-11-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200918_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='foodreview',
            name='created_date',
        ),
        migrations.AddField(
            model_name='store',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='deleted_date',
            field=models.DateTimeField(null=True),
        ),
    ]
