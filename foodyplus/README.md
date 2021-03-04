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
