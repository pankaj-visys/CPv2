# Generated by Django 4.1.3 on 2023-01-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_remove_ppr_slugn_ppr_new_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='que',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
