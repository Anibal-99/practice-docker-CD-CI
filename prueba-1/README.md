# Prueba-1 
Diagrama de Red Produzca un diagrama de red (puede utilizar
lucidchart) de una aplicación web en GCP o AWS y escriba una descripción de
texto de 1/2 a 1 página de sus elecciones y arquitectura.
El diseño debe soportar:
- Cargas variables
- Contar con alta disponibilidad
- Frontend en JS
- Backend con una base de datos relacional y un no relacional
- La aplicación backend consume 2 microservicios externos

El diagrama debe hacer un mejor uso de las soluciones distribuidas.


## Resolucion 
![](/prueba-1/AWS-network-diagram.png)

En la resolucion del diagrama de red, lo que hice fue investigar en diferentes fuentes en google hasta que encontre una guia proporcionada por la pagina de AWS, la cual consiste en implementar una aplicacion en node. Por aqui dejo el link para que se pueda visitar.
- [Deploy a Node.js web application](https://aws.amazon.com/es/getting-started/hands-on/deploy-nodejs-web-app/)

En conjunto con esta guia lo que hice fue seguir investigando para lograr crear el diagrama de la mejor manera de acuerdo a lo solicitado en el ejercicio. 

## Herramientas utilizadas
- **Route 53**: Este es el servicio donde se define toda la configuracion de DNS. 
- **Load balancer**: Distribuye las diferentes solicitudes que van llegando en las instancias de EC2 que estan corriendo las aplicaciones. Esto que se conoce como load balancer, es lo que usamos como NGINX, un usuario envia un a peticion al load balancer y lo distribuye en los servidores backend.
- **Amazon DynamoDB**:Servicio para base de datos de NoSql. Diseñada para ejecutar aplicaciones de alto rendimiento a cualquier escala, ofrece seguridad, copias continuas, entre muchas otras.
- **AmazonRDS**:Servicio de administracion de base de datos relacional, pueden utilizarse seis motores de bases de datos, MySql, MariaDB, postgreSQL, Oracle, microsoft SQL server y Amazon Aurora. 
- **Auto Scaling**: Si la carga aumenta en las instancias de EC2, entonces puede escalar horizontalmente automanticamente y si la carga disminuye puede hacerlo verticalmente. Sirve para aumentar la cantidad de servidores de aplicacion ayudando asi a mantener la disponibilidad. 
- **Bucket**: Brinda seguridad y disponibilidad de los datos. Sirve de intermediario entre las aplicaciones y la base de datos relacional y la no relacional.
- **ElastiCache**: Servicio que ayuda a aumentar el rendimiento en las busquedas de elementos que son bastante comunes. Esto ayuda a reducir la exigencia sobre la base de datos y aumenta la escalabilidad de la aplicacion.

## Links utilizados para llevar a cabo el ejercicio.
- [Deploy a Node.js web application](https://aws.amazon.com/es/getting-started/hands-on/deploy-nodejs-web-app/)
- [Intro to AWS - The Most Important Services To Learn](https://www.youtube.com/watch?v=FDEpdNdFglI&t=1282s)
- [AWS services](https://www.youtube.com/watch?v=Z3SYDTMP3ME&t=1561s)
- [Auto Scaling](https://www.ilimit.com/blog/como-funciona-autoscaling/)
- [Web Application Architecture](https://medium.com/geekculture/web-application-architecture-800d3ecd8019)
- [Microservicios](https://aws.amazon.com/es/microservices/)

## Microservicios
Adicionalmente en la prueba se menciona que el backend debe consumir 2 microservicios. Como no encontraba una informacion que me diera confianza y que entendiera como se diagrama decidi no incluirlo. De todas maneras los intente diagramar, adjunto el link por si se desea visualizar como lo implemente. 
- [Implementacion de microservicio](https://lucid.app/lucidchart/0c5a3584-411d-4bf9-bddd-95a1d6f799c2/edit?viewport_loc=1748%2C12%2C3214%2C1646%2CeNbqbEM6f5NI&invitationId=inv_0ecc56c4-2440-4f18-8aa4-bea2a03d3c10)