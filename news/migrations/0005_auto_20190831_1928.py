# Generated by Django 2.2.2 on 2019-08-31 13:43

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('news', '0004_auto_20190830_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
    ]
