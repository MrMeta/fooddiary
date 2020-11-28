# Generated by Django 3.1.1 on 2020-11-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20201128_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='deleted_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='foodreview',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='foodreview',
            name='deleted_date',
            field=models.DateTimeField(null=True),
        ),
    ]