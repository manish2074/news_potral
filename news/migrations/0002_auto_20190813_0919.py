# Generated by Django 2.2.2 on 2019-08-13 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[('0', 'Politics'), ('1', 'Sports'), ('2', 'Fashion'), ('3', 'Technology')], max_length=2),
        ),
    ]
