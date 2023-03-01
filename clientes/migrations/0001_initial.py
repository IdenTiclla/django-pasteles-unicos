# Generated by Django 4.1.7 on 2023-02-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=8)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
    ]
