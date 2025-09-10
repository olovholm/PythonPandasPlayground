# Analytics with Python and Pandas


### Overview

### Setup
The infrastructure for this project is using Postgres and Airflow through Docker. 

To access the database from the airflow container you will have to create an env-file (here named docker.env) with the following variables:

```env

DB_USER=stagetest
DB_PASSWORD=stagetest
DB_NAME=stagetest
DB_SERVER=db
```

For initial setup run the following commands:

```bash
docker compose run airflow-webserver airflow db init  

docker compose run airflow-webserver airflow users create \
  --username airflow --firstname Airflow --lastname Admin \
  --role Admin --email admin@example.com --password airflow
  
```

For further running of the services use.
```bash
docker  docker compose --env-file docker.env up -d
```
