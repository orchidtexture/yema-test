# yema-test Docker Compose

## Development

|Service| Service Name | Port |
|---|---|---|
| db | yema-test_db_1 | 5432 |
| web | yema-test_web_1 | 8000 |

## Production

|Service| Service Name | Port |
|---|---|---|
| db | yema-test_db_1 | 5432 |
| web | yema-test_web_1 | 8000 |
| nginx | nginx_1 | 1337 |

## Setting everything up

1. Install docker https://www.docker.com/get-docker
2. Install docker-compose https://docs.docker.com/compose/install/
3. Start the **docker-compose** service.

### Production

4. Build services `docker-compose -f docker-compose.prod.yml up -d --build`
5. Migrate `docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput`
6. Collect statics `docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear`
* **url** - http://localhost:1337/

## Basic Usage

### Development

- Build all services `docker-compose up --build`

- Start all services `docker-compose up`

- Stop all services `docker-compose stop`

- Open the shell `docker-compose exec web /bin/sh`

### Production

- Build all services `docker-compose -f docker-compose.prod.yml up --build`

- Start all services `docker-compose -f docker-compose.prod.yml up`

- Stop all services `docker-compose -f docker-compose.prod.yml stop`

- Open the shell `docker-compose -f docker-compose.prod.yml exec web /bin/sh`

## Django tests
```
$ docker-compose exec web python manage.py test appointments/tests
```

## Coverage
- Run tests `docker-compose run web coverage run manage.py test appointments/tests`
- Generate report `docker-compose run web coverage report -m`

## Docs

* **yema-test API** - http://localhost:8000/docs/
* **HTTP Status Codes** - https://www.restapitutorial.com/httpstatuscodes.html