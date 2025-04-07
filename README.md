# Mongo_proyectos
Quick descripcion about the structure and general content of each proyect.

1. FastAPIs and Mongo Atlas.
    What is it?
    CRUD using MongoDB atlas and FastAPI, and a API propuesta por mi, es este caso la idea es...

    How does the stucture work?
    We have 4 main folders.
    1. db: holds the connection script to the Atlas cluster.
    2. models: here we have the script that holds the structure of our data "tables", ex: product, user, etc.
    3. routes: we define the responses for a group of specific routes "/.../", basically we set up the APIs behaviour depending on which path we use to access it.
    4. services: we have our accions, methods or services (however u wanna call it), escencialmente definimos las acciones que se pueden hacer con los datos alojados en nuestro cluster, encerradas en metodos especificos, ex: create_user, find_product, etc.