# Generated by Django 2.0.6 on 2021-08-07 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0004_auto_20210807_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='employee_name',
            new_name='emp',
        ),
    ]