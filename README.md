# Analytics with Python and Pandas


### Overview

### Setup
The infrastructure for this project is using Postgres and Airflow through Docker. 
For initial setup run the following commands:

```bash
docker compose run airflow-webserver airflow db init  

docker compose run airflow-webserver airflow users create \
  --username airflow --firstname Airflow --lastname Admin \
  --role Admin --email admin@example.com --password airflow

docker compose up -d
```
