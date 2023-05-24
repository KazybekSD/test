# Generated by Django 4.2.1 on 2023-05-24 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sma', '0020_delete_costitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrCostItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Наименование элемента затрат')),
            ],
            options={
                'verbose_name': 'Элемента затрат',
                'verbose_name_plural': 'Элементы затрат',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CostItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Наименование статьи затрат')),
                ('gr_cost_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sma.grcostitem', verbose_name='Элемент затрат')),
            ],
            options={
                'verbose_name': 'Статью затрат',
                'verbose_name_plural': 'Статьи затрат',
                'ordering': ['id'],
            },
        ),
    ]