# Prueba-3
**CI/CD**

Dockerizar un nginx con el index.html default. Elaborar un pipeline que ante cada cambio realizado sobre el index.html buildee la nueva imagen y la actualize en la plataforma elegida. (docker-compose, swarm, kuberenetes, etc.)Para la creacion del CI/CD se puede utilizar cualquier plataforma (CircleCI, Gitlab, Github, Bitbucket.)

**Requisitos y deseables**:

La solución al ejercicio debe mostrarnos que usted puede:
- Automatizar la parte del proceso de despliegue. usar conceptos de CI para aprovisionar el software necesario para que los entregables se ejecuten use cualquier
herramienta de CI de su elección para implementar el entregable.

## Solución

Para empezar primero lo que hice fue dockerizar el nginx, es decir, cree un dockerfile con la imagen oficial de ngix, esto lo hice mirando el docker hub [link](https://hub.docker.com/_/nginx) en un parte de mas abajo se muestra como crear el docker file.

Luego cree el directorio html dentro del directorio prueba-3 y cree un nuevo archivo index.html que cuando se le haga algun cambio y luego hagamos un push, se va a buildear y se va a actualizar con github actions.

Utilice github actions ya que trabaje con todos los demas ejecicios en github.

## Actividades realizadas
- Cree el archivo push.yml dentro de la carpeta .github/workflows, en el cual define la estructura del pipeline, los trabajos y los pasos que debera ejecutar al momento de realizar un push al repositorio de github.
- Luego lo que hice fue crear los secrets en la configuracion del repositorio, en los cuales especifique mi usuario y el token de acceso a mi docker hub.
- Adicionalmente tuve varios problemas en los primero push que realice, problemas con la estructura y los pasos que habia definido en el push.yml, busque en google algunos de los erroes y otros intente entender primero por mi cuenta que es lo que estaba pasando, a ver si lograba solucionarlo.

## Links
Algunas referencias de los videos que mire para informarme sobre github actions:
- [Build and push Docker images](https://github.com/marketplace/actions/build-and-push-docker-images#git-context)
- [GitHub Actions TUTORIAL Desde Cero](https://www.youtube.com/watch?v=sIhm4YOMK6Q&t=127s)
- [Deploying a Web App with Docker & Github Actions](https://www.youtube.com/watch?v=JsOoUrII3EY)
- [Github Actions - CI/CD Gratuito y fácil en Github](https://www.youtube.com/watch?v=MNBf-ylhtK0&t=479s)
