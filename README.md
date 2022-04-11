# Paidy-code-challenge

## How to setup local environment

### Database
To startup database, run `docker compose up`. 
This will bring up a container with MySQL and bind the volumes so that data can be persisted locally. 

A build script was not done for this challenge, so it might be needed to bash into the container and run `chown -R mysql:mysql /var/lib/mysql`.

For the first login into the application, it is necessary to manually bash into the container and run the database migrations:
``` sh
    mysql -u root -p

    USE restaurant
    SOURCE /scripts/1-database_create.sql

```

### Api

For the first run, please ensure both `pipenv` and `python 3.10` are installed. then run `pipenv install --dev`.

ensure that you have a `.env` file under server directory to tell the api the location of the database:

```
    MYSQL_USER=root
    MYSQL_PASSWORD=1234
    MYSQL_PORT=3400
    MYSQL_HOST=localhost
```

To start the api run `pipenv run api`.

### Client 

For the first run, please ensure that both `node` and `yarn` are installed (alternatively, `npm` can be used).
ensure that you have a `.env` file under client directory to tell location of the api:

```
    NEXT_PUBLIC_ORDER_HOST=http://localhost:8000
```

to start the api in development mode, run `yarn dev`