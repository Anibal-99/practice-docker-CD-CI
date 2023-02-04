# Prueba-2
**Despliegue de una aplicación Django y React.js**
- Elaborar
el deployment dockerizado de una aplicación en django (backend) con frontend
en React.js contenida en el repositorio. Es necesario desplegar todos los servicios
en un solo docker-compose.

- Se deben entregar los Dockerfiles pertinentes para elaborar el despliegue y justificar la forma en la que elabora el deployment (supervisor, scripts, dockercompose, kubernetes, etc)

- Subir todo lo elaborado a un repositorio (github, gitlab, bitbucket, etc). En el
repositorio se debe incluir el código de la aplicación y un archivo README.md
con instrucciones detalladas para compilar y desplegar la aplicación, tanto en
una PC local como en la nube (AWS o GCP).

## Solución
Debemos colocarnos dentro del directorio prueba-2, donde encontraremos el docker-compose para ejecutar.

Para levantar la aplicacion ejecutaremos los siguientes comandos;
- El siguiente comando lo que hace es construir las imagenes;

```
docker-compose build
```
- Luego para levantar los contedores se hace con el comando;
```
docker-compose up
```
- Tambien podemos simplificar estos dos comandos en uno solo, es decir, construir las imagenes y luego levantar;
```
docker-compose up --build
```
Para ver la aplicacion corriendo debemos ingresar en el navegador y indicar nuestro host con los puertos correspondientes.

- Para el backend.
```
127.0.0.1:8000
```
- Para el frontend.
```
127.0.0.1:3000
```
Si desea realizar algun comando en el backend en su aplicacion mientras esta levantada, puede hacerlo con el siguiente comando;
```
docker-compose run --rm backend sh -c "comando"
```
## Observaciones
Para llevar a cabo el ejecicio tuve que investigar como se creaba el Dockerfile correspondiente para el fronend, ya que anteriormente nunca habia echo uno. Para el lado del backend ya habia dockerizado mis aplicaciones personales, con lo que ya sabia como hacerlo.

Para aprender sobre el Dockerfile del frontend utilice el siguiente post, [How to Dockerize a Django and React Application](https://www.honeybadger.io/blog/docker-django-react/)

### Errores encontrados
- Al momento de levantar la aplicacion me di cuenta que estaba configurado para que la secret_key no estuviera vacia, entonces lo que hice fue crear un archivo secret.py en el directorio ./backend y genere una secret_key. Luego queria buscar la forma de implementarla en el docker-compose, asique encontre una forma sencilla de hacerlo, siguiendo este post [docker-compose and django secret key](https://stackoverflow.com/questions/69381652/docker-compose-and-django-secret-key)
- Otro errores que tuve que buscar era del lado del backend con graphviz **pygraphviz**, entonces lo que hice fue buscar de que manera podia solucionar ese error y encontre una manera de hacerlo en stackoverflow, [link](https://stackoverflow.com/questions/40528048/pip-install-pygraphviz-no-package-libcgraph-found)
- Tambien tenia errores con el adaptador de la base de datos postgreSQL, asique lo que hice fue buscar el error, pero en este caso solo tuve que comentar una de las librerias de psycopg2.
