# Generated by Django 3.0.6 on 2020-06-24 22:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_remove_blog_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
