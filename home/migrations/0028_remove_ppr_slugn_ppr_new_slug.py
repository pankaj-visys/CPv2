# Generated by Django 4.1.3 on 2023-01-09 05:21

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_ppr_slugn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ppr',
            name='slugn',
        ),
        migrations.AddField(
            model_name='ppr',
            name='new_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
