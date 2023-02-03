FROM node:19-alpine3.16

# directorio de trabajo
WORKDIR /app/frontend

COPY . /app/frontend
# copia el directorio del front en el directorio de trabajo

# expone el puerto 3000
EXPOSE 3000

# instala las dependencias
RUN npm install 

# levanta el proyecto
CMD ["npm", "start"]