# Generated by Django 3.1.1 on 2020-09-18 02:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200918_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.food')),
            ],
        ),
    ]