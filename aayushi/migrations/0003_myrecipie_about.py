# Generated by Django 3.0.7 on 2020-08-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aayushi', '0002_auto_20200802_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='myrecipie',
            name='about',
            field=models.CharField(default='watch recipie', max_length=20),
        ),
    ]
