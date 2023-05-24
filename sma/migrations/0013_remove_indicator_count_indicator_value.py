# Generated by Django 4.2.1 on 2023-05-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sma', '0012_alter_service_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicator',
            name='count',
        ),
        migrations.AddField(
            model_name='indicator',
            name='value',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=10, verbose_name='Значение'),
            preserve_default=False,
        ),
    ]