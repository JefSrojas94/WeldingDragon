# Generated by Django 4.1.1 on 2022-09-13 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_de_usuario', models.CharField(max_length=30, verbose_name='Tipo de Usuario')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Nombre de Usuario')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('cedula', models.CharField(max_length=12, verbose_name='Cedula')),
                ('correo', models.EmailField(max_length=100, verbose_name='Email')),
                ('tipo_de_Cliente', models.CharField(max_length=20, verbose_name='Tipo de cliente')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
