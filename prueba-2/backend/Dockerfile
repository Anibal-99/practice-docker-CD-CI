FROM python:3.8

# muestra la salida de la consola, los logs
ENV PYTHONUNBUFFERED 1

# copio el archivo requirements en el contenedor en la direccion especificada
COPY ./requirements.txt /tmp/requirements.txt

# copio la carpeta del backend en app
COPY . /app/api
# directorio de trabajo, app
WORKDIR /app/api
# especifico que puerto es el que se expone
EXPOSE 8000

# para que se instalen las nuevas dependencias que agreguemos en nuestro requirements.txt
RUN python -m venv /py && \
    apt-get update && \
    apt-get install -y graphviz libgraphviz-dev pkg-config && \
    /py/bin/pip install --upgrade pip && \
    #lo instalamos en el directorio temporal /tmp ya que una ves que instalamos las dependencia luego no lo necesitamos
    /py/bin/pip install -r /tmp/requirements.txt && \ 
    rm -rf /tmp && \
    pip install pygraphviz && \
    #para que no nos cree un usuario, ya que si no especificamos esta linea no podremos hacer cambios desde nuestro host al contenedor, porque necesitariamos hacerlo como root.
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

# Esta linea debe ser siempre la ultima de nuestro dockerfile, todo lo que se ejecuto hasta el momento se hizo como root y con esta linea especificamos al usuario que vamos a cambiar, que es el usuario django.
USER django-user
