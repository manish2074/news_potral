# Generated by Django 2.2.2 on 2019-09-01 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_merge_20190901_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[('0', 'Politics'), ('1', 'Fashion'), ('2', 'Business'), ('3', 'Sports')], max_length=2),
        ),
    ]
