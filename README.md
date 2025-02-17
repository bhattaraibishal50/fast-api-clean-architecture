# fast-api-clean-architecture

Fast API Clean Architecture template with docker, nginx, postgres, pgadmin4
<br/>

## Instructions

Run below commands to your terminal

```bash
COPY .env.example .env #copy sample env to .env
```

```bash
docker-compose up --build #build and spin docker containers
```

```bash
make migrate-up # to migrate migrations
```

- API DOCS : http://localhost/docs
- adminer: http://localhost:5050

Check `Makefile` for available commands

## Features

- [x] Docker
- [x] mysql
- [x] adminer
- [x] Dependency injection
- [x] SqlAlchemy as ORM
- [x] Poetry to manage python packages
- [x] Alembic for migrations
- [x] pydantic data validation
- [x] User model
- [x] User authentication
- [x] Exception handling
- [x] CORS middlware
- [x] Error handling
