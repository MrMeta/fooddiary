# Generated by Django 3.1.1 on 2020-09-18 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_foodreview_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodreview',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]