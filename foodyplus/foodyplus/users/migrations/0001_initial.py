# Generated by Django 3.1 on 2021-03-02 16:41

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foods', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('email', models.EmailField(error_messages={'unique': 'Ya existe un usuario con este email'}, max_length=254, unique=True, verbose_name='Direccion de email')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='El numero de celular tiene que tener el formato: +999999999. Hasta 15 digitos', regex='\\+?1?\\d{9,15}$')])),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('account_type', models.CharField(blank=True, choices=[('C', 'Cliente'), ('A', 'Admin')], default='C', max_length=1, null=True, verbose_name='Tipo de cuenta')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ShippingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('first_name', models.CharField(max_length=30, verbose_name='Nombre del perfil')),
                ('last_name', models.CharField(max_length=30, verbose_name='Apellido del perfil')),
                ('country', models.CharField(max_length=30, verbose_name='Pais donde vive')),
                ('street_address', models.CharField(max_length=30, verbose_name='Direccion de la calle')),
                ('apartament', models.CharField(blank=True, max_length=30, null=True, verbose_name='Apartamente donde vive')),
                ('city', models.CharField(max_length=50, verbose_name='Ciudad donde vive')),
                ('state', models.CharField(max_length=30, verbose_name='Estado/provincia donde vive')),
                ('zip_code', models.IntegerField(verbose_name='Codigo postal')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/pictures/', verbose_name='imagen de perfil')),
                ('biografy', models.TextField(blank=True, max_length=500, verbose_name='Biografia del perfil')),
                ('points', models.IntegerField(blank=True, default=0, verbose_name='Cantidad de puntos acumulados')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='fav_list',
            field=models.ManyToManyField(through='users.Favorite', to='foods.Recipe'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
