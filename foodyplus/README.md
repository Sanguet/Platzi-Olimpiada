# FoodyPlusAPI

![](https://img.shields.io/github/forks/Sanguet/Platzi-Olimpiada) ![](https://img.shields.io/github/commit-activity/w/Sanguet/Platzi-Olimpiada) ![](https://img.shields.io/github/last-commit/Sanguet/Platzi-Olimpiada)

**FoodyPlusAPI** es el proyecto del equipo **Switch** para la competencia **Olympia Challenge** de **Platzi**

## Comenzando 🚀

Estas instrucciones te permitirán obtener una **copia** del proyecto en **funcionamiento** en tu máquina **local** para propósitos de **desarrollo y pruebas**.

Mira **Deployment** para conocer como desplegar el proyecto.

### Pre-requisitos 📋

Necesitas tener **Docker** y una terminal de linux, recomendamos **Ubuntu**

```
https://docs.docker.com/docker-for-windows/install/
https://www.itechguides.com/how-to-install-ubuntu-on-windows-10/
```

### Instalación 🔧

Ya que estamos usando Docker sera una instalacion super sencilla y rapida

Lo primero es bajar el repositorio de gitHub

```
git clone https://github.com/Sanguet/Platzi-Olimpiada.git
```

Lo siguiente sera ir al directorio donde se encuentra el proyecto

```
cd Platzi-Olimpiada/foodyplus/
```

Ahora haremos el **build** de docker(puede agregar "sudo" si lo requiere)

```
docker-compose -f local.yml build
```

Ya que tenemos el entorno montado, solo queda correr las migraciones de django

```
docker-compose -f local.yml run --rm django python manage.py migrate
```

Si lo requieres puedes crear tu propio **superuser** para testear y manejar la api

```
docker-compose -f local.yml run --rm django python manage.py createsuperuser
```

Ademas tendras que darle permisos especiales

```
docker-compose -f local.yml run --rm django python manage.py shell
	from foodyplus.users.models import User, Profile
	user = User.objects.get()
	user.account_type = 'A'
	user.save()
	Profile.objects.create(user=user)
	exit
```

Ahora ya tienes todo lo necesario, prueba ir a **localhost:8000/users/login/** y logea con tus credenciales anteriormente puestas en el superuser

## Arquitectura DB
La siguiente imagen explica a gran escala la db:
![](https://foodyplus.s3-sa-east-1.amazonaws.com/ARQUITECTURA+DB.png)

Este es un link directo a la imagen:
**https://foodyplus.s3-sa-east-1.amazonaws.com/ARQUITECTURA+DB.png**

**User:** 
- Id_wish_list: Es un campo muchos a muchos entre user y recipe, para que se guarden en la lista de desos/favoritos
- username: Es un campo unico de identificacion del usuario
- email: Es el campo unico de email para logearse y recibir emails
- password: Es el campo que almacena la contraseña, esta se guarda en HASH256, NO se muestra en texto plano
- account_type: es un campo choice que tiene las opciones de "Client" y "Admin" para distingir a los usuarios.
- phone_number: Es un campo hecho para almacenar el numero del usuario, tiene un validador con expresion regular.

**favorite**
- id_user: Foreing_key para el usuario
- id_recipe: Foreing_key para la receta

**shipping_info:**
- id_user: Es un foreing_key para user, la misma puede ser null y salteada en el form , esta hecha para que la informacion de envio pueda ser linkeada con un usuario y no tener que repetirla, ademas de permitir tener varias direcciones.
- Todos los demas campos son obligatorios para el envio de paquetes, no tienen nada de especial

**cupon**
- id_user: Es un foreing_key para user, es obligatoria, ya que solo los usuarios puede tener un cupon y son unicos para cada usuarios.
- name: Nombre del cupon
- code: Codigo unico del cupon
- discount: Descuento del cupon expresado en *100* como entereros se toma como $100 de descuento, si se expresa en *0.1* se toma como 10%
- exp_date: Es la fecha en que vence el cupon, por defecto los cupones duran un solo dia.
- comment: Comentario de la venta si lo llega a tener, pero no es obligatorio
- delivery_charge: Cargo de envio de la venta
- finalize: Es un campo para ver el estado de la venta, si fue finalizada o sigue activa.
- tracking_code: Codigo de trackea, se genera aleatoriamente y tiene 10 caracteres.

**sale**
- id_user: Es un foreing_key para user, la misma puede ser null y salteada en el form, tiene la funcion de linkear la venta con el usuario.
- id_detail: Es un campo muchos a muchos entre Sale y Product.
- id_shipping_info: Es un foreing_key para shipping_info, la misma puede ser null y saltada en el form, ya que para crear el carrito no necesitamos la shipping info.
- discount: Descuento de la venta, si hay un cupon lo setea el cupon.
- payment_method: Un campo choice que guarda el metodo de pago usado.
- total: Es el total de la venta
- steps: Es un choice que setea el estado en que se encuentra el pedido para el seguimiento.
- delivery_date: Fecha en la que deberia de llegar el pedido al cliente, por defaul se setea en una semana hacia adelante.

**sale_detail**
- id_sale: Es el foreing_key de sale
- id_product: Es el foreing_key de product
- amount: Es la cantidad del producto que se va a agregar
- discount: Es el descuento del producto
- sub_total: Es el monto del producto, es una multiplicacion entre el amount y price del product

**product**
- id_category_product: Es una foreing_key para product_category, setea la categoria del producto
- name: nombre del producto
- cost: Costo del producto
- price: Precio del producto
- provide: Proveedor del producto
- barcode: codigo de barra del producto
- stock: Inventario del producto.
- discount: Descuento por default del producto, su principal es poner ofertas por temporada al producto en si.
- unit_sales: unidades vendidas del producto, registro historico
- unit: Unidad de medidad del producto.

**product_category**
- name: Nombre de la categoria
- comment: Comentario de la categoria
- usages: Numero de veces que se uso la categoria, esta ahi mas que todo para metricas

**recipe**
- id_category: Foreing_key para recipe_category, es obligatorio
- id_detail: Campo muchos a muchos entre recipe y product, ya que los productos de una receta son diferentes al producto en si
- id_comment: Campo muchos a muchos entre recipe y user, es para que los usuarios puedan comentar en las recetas.
- description: Description de la receta.
- name: Nombre unico de la receta.
- video: Video de la receta, se guarda como un URL
- country: Pais de donde se obtuvo la receta
- total_time: Tiempo que lleva preparar toda la receta.
- likes: Numero de me gusta que tiene la receta, aumenta cuantos mas usuarios la agregen a favoritos.
- porcions: Numero de porciones de la receta.
- preparation: Preparacion de la receta.
- picture: Imagen de la receta, la misma se guarda en s3
- price: Precio final de la receta

**recipe_category**
- name: Nombre de la categoria
- comment: Comentario de la categoria.
- icon: Icono de la categoria

**recipe_detail**
- id_recipe: Foreing_key para la receta
- id_product: Foreing_key para el producto
- unit: Unidades del producto que lleva la receta, mas que todo para mostrarlo en el front.
- amount: Cantidad del producto que lleva la receta
- discount: Descuento que pueda llegar a tener ese producto por festejos.
- sub_total: Monto total del producto con esa cantidad para la receta.

**recipe_comment**
- id_user: Foreing_key para user
- id_recipe: Foreing_key para la receta
- comment: Comentario del usuario en la receta

**planning**
- id_user: Foreing_key para el user.
- id_detail: Campo muchos a muchos entre planning y recipe, ya que en una planificacion pueden ir muchas recetas y muchas recetas pueden tener muchas planificaciones al mismo tiempo.
- name: Nombre de la planificacion
- formar: Es un campo choice para setear si es una planificacion semanal o mensual
- description: Descripcion de la planificacion

**plannging_detail**
- id_planning: Foreing_key para la planificacion
- id_recipe: Foreing_key para la receta
- day: Dia de la semana o mes en que se coloca la receta
- time: Es un campo choice para setear si es almuerzo, cena, merienda, desayuno

**basic_model**
- created:  Campo de fecha, se genera solo con la fecha del momento
- modified: Campo que se actualiza cada vez que se actualiza el modelo
- is_active: Campo que setea si el modelo esta activo o no, es un boolean


## Despliegue 📦

El deploy se puede realizar con cualquier servicio cloud que maneje maquinas virtuales **linux**, solo hay que instalar git, docker y docker-compose para poder **buildear** el proyecto y agregar las configuraciones de **produccion**

## Construido con 🛠️

Vamos a dar menciones a algunos frameworks/librerias que utilizamos, ya que todos los frameworks/librerias estan en el archivo **requirements**.

- [Django](https://www.djangoproject.com/) - El framework de python mas usado en backend
- [Django REST Framework](https://www.django-rest-framework.org/) - El framework mas usado para la creacion de APIs en python
- [SimpleJWT](https://github.com/SimpleJWT/django-rest-framework-simplejwt) - Usado para generar y manipular los JWT
- [Celery](https://github.com/celery/celery/) - Utilizado para el control de tareas asincronas y manejo de cache
- [Django Anymail](https://github.com/anymail/django-anymail) - Utilizado para manipular el envio de mails

## Contribuyendo 🖇️

Cualquier PR que se haga sera revisado por el equipo dev principal.

## Autores ✒️

Estos fueron los autores que contribuyeron a lo largo del proyecto.

- **Oyarzabal Ivan\*** - _Desarrollo_ - [Sanguet](https://github.com/Sanguet)
- **Oyarzabal Ivan\*** - _Deploy_ - [Sanguet](https://github.com/Sanguet)
- **Oyarzabal Ivan\*** - _Documentacion_ - [Sanguet](https://github.com/Sanguet)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/Sanguet/Platzi-Olimpiada/blob/master/foodyplus/CONTRIBUTORS.txt) quíenes han participado en este proyecto.

## Expresiones de Gratitud 🎁

- Se agradece enormemente a **Platzi** por brindarnos la oportunidad de participar en esta competencia 📢
- De igual forma se agradece a **todo** el **equipo** de **desarrollo** de **Switch**, **no importa que sean de distintas areas**, todos **contribuyeron** para formar esto. ⭐️
- Y le agradecemos a todo aquel que se haya tomado la molestia de leer hasta aqui 🤓..

---

⌨️ con ❤️ por [Sanguet](https://github.com/Sanguet) 😊