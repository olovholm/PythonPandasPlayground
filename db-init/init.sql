-- db-init/init.sql
CREATE DATABASE stagetest;
CREATE USER stagetest WITH ENCRYPTED PASSWORD 'stagetest';
GRANT ALL PRIVILEGES ON DATABASE stagetest TO stagetest;

\c stagetest
-- Change ownership of the public schema
ALTER SCHEMA public OWNER TO stagetest;


CREATE DATABASE airflow;
CREATE USER airflow WITH ENCRYPTED PASSWORD 'airflow';
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;

\c airflow
-- Change ownership of the public schema
ALTER SCHEMA public OWNER TO airflow;
