# Generated by Django 2.1.1 on 2018-10-26 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adoptante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name': 'Adoptante',
                'verbose_name_plural': 'Adoptantes',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('fechaIngreso', models.DateField(max_length=10)),
                ('fechaNacimiento', models.DateField(max_length=10)),
                ('descripcion', models.CharField(max_length=50)),
                ('model_pic', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
            ],
            options={
                'verbose_name': 'Mascota',
                'verbose_name_plural': 'Mascotas',
            },
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=50)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ciudad')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regiones',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vivienda', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Raza'),
        ),
        migrations.AddField(
            model_name='mascota',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tipo'),
        ),
        migrations.AddField(
            model_name='adoptante',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
        migrations.AddField(
            model_name='adoptante',
            name='vivienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Vivienda'),
        ),
    ]
