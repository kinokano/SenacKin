# Generated by Django 4.2.19 on 2025-03-07 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoresCascade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('dataNascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='AutoresProtect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('dataNascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LivrosProtect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('anoPublicacao', models.DateField()),
                ('idAutor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teste.autoresprotect')),
            ],
        ),
        migrations.CreateModel(
            name='LivrosCascade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('anoPublicacao', models.DateField()),
                ('idAutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teste.autorescascade')),
            ],
        ),
    ]
