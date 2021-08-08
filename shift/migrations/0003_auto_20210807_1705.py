# Generated by Django 2.0.6 on 2021-08-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0002_auto_20210807_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='名前'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
