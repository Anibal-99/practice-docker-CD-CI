# mediante las siguientes lineas lo que hice fue generar el secret_key, ya que esta no puede estar vacia
# segun la configuracion, entonces lo genere y el resultado esta en .env 
# luego al momento de crear el docker compose se setea la variable de entorno con el valor que esta en .env
import secrets
print(secrets.token_hex(25))
