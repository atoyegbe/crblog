# Generated by Django 3.0.3 on 2020-04-11 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
