# Generated by Django 3.2.18 on 2023-05-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_comision_personau'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstudianteAbs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=150, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=150, null=True)),
                ('dni', models.IntegerField(verbose_name='DNI')),
                ('matricula', models.CharField(max_length=10, verbose_name='Matricula')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstructorAbs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=150, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=150, null=True)),
                ('dni', models.IntegerField(verbose_name='DNI')),
                ('legajo', models.CharField(max_length=10, verbose_name='Legajo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]