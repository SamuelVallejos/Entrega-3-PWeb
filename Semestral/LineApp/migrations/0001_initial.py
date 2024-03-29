# Generated by Django 4.0.4 on 2022-05-26 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del usuario')),
                ('nick', models.CharField(max_length=20, verbose_name='Nickname de usuario')),
                ('correo', models.CharField(max_length=100, verbose_name='Correo electronico del usuario')),
                ('contra', models.CharField(max_length=20, verbose_name='Contraseña del usuario')),
            ],
        ),
    ]
