# Generated by Django 4.2.1 on 2023-05-23 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sma', '0003_servicetype_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicetype',
            options={'ordering': ['id'], 'verbose_name': 'Вид услуг', 'verbose_name_plural': 'Виды услуг'},
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
