# Generated by Django 4.2.19 on 2025-03-04 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastos',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='gastos',
            name='horario',
            field=models.TimeField(),
        ),
    ]
