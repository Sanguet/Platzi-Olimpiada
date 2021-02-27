# Generated by Django 3.1 on 2021-02-27 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('code', models.CharField(max_length=13, unique=True, verbose_name='Codigo del cupon')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Descuento del cupon')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la etiqueta')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la planificacion')),
                ('date', models.CharField(blank=True, choices=[('S', 'Semanal'), ('M', 'Mensual')], default='S', max_length=1, verbose_name='Tipo de planificacion')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Descripcion de la planificacion')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlanningDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('day', models.IntegerField(verbose_name='Dia de la semana o del mes')),
                ('time', models.CharField(choices=[('D', 'Desayuno'), ('A', 'Almuerzo'), ('M', 'Merienda'), ('C', 'Cena')], max_length=1, verbose_name='Tipo de planificacion')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Costo del producto')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Precio del producto')),
                ('stock', models.IntegerField(blank=True, default=0, verbose_name='Inventario del producto')),
                ('provider', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre del proveedor')),
                ('barcode', models.BigIntegerField(blank=True, null=True, verbose_name='Codigo del producto')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, verbose_name='Descuento del producto')),
                ('description', models.TextField(blank=True, max_length=700, null=True, verbose_name='Descripcion del producto')),
                ('comment', models.TextField(blank=True, max_length=700, null=True, verbose_name='Comentario del cliente')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='foods/pictures/', verbose_name='imagen del producto')),
                ('units_sales', models.IntegerField(blank=True, default=0, verbose_name='Numero de ventas hechas de este producto en el mes')),
                ('unit', models.CharField(blank=True, max_length=10, null=True, verbose_name='Unidad de venta')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre de la categoria')),
                ('comment', models.TextField(blank=True, max_length=500, verbose_name='Comentario de la categoria')),
                ('usages', models.IntegerField(blank=True, default=0, verbose_name='Numero de veces que se uso la categoria en el mes')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la receta')),
                ('video', models.URLField(blank=True, max_length=500, null=True, verbose_name='Link del video de la receta')),
                ('utensils', models.TextField(blank=True, max_length=500, null=True, verbose_name='Utencilios utilizados')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Pais de origen de la receta')),
                ('total_time', models.IntegerField(blank=True, null=True, verbose_name='Tiempo que se demora en preparar la receta')),
                ('likes', models.IntegerField(blank=True, default=0, verbose_name='Numero de likes que tiene la receta')),
                ('portions', models.IntegerField(blank=True, null=True, verbose_name='Numero de raciones')),
                ('description', models.TextField(blank=True, max_length=700, null=True, verbose_name='Descripcion de la receta')),
                ('comment', models.TextField(blank=True, max_length=700, null=True, verbose_name='Comentario de la receta')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la categoria')),
                ('comment', models.TextField(blank=True, max_length=500, verbose_name='Comentario de la categoria')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecipeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('amount', models.PositiveIntegerField(blank=True, default=1, verbose_name='Cantidad del producto')),
                ('unit', models.CharField(blank=True, max_length=10, null=True, verbose_name='Unidad de venta')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, verbose_name='Descuento del producto en la receta')),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Sub total')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecipeLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, verbose_name='Descuento del producto')),
                ('payment_method', models.CharField(blank=True, choices=[('C', 'Contado'), ('D', 'Debito'), ('T', 'Credito')], default='C', max_length=1, verbose_name='Tipo de metodo de pago')),
                ('total', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Total')),
                ('delivery_charge', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Costo de envio')),
                ('delivery_date', models.DateTimeField(verbose_name='Fecha en la que debe ser entregado')),
                ('steps', models.CharField(blank=True, choices=[('P', 'Preparandose'), ('E', 'En camino'), ('R', 'Recibido')], default='P', max_length=1, verbose_name='Seguimiento de la venta')),
                ('comment', models.TextField(blank=True, max_length=500, null=True, verbose_name='Comentario de la venta')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('amount', models.PositiveIntegerField(blank=True, default=1, verbose_name='Cantidad del producto')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, verbose_name='Descuento del producto')),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Sub total')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('recipes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.recipe')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
