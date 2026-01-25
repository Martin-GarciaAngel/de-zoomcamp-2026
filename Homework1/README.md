# Data Engineering Zoomcamp 2026 - Module 1

This repository contains my homework submissions for the first module of the DE Zoomcamp.

## Contents
* **Homework1/**: Docker, SQL, and Terraform tasks.
  * `ingest_data.py`: Script to load taxi trip data into Postgres.
  * `ingest_zones.py`: Script to load taxi zone lookup data.
  * `docker-compose.yaml`: Infrastructure setup for Postgres and pgAdmin.

## How to run
1. Start the infrastructure: `docker-compose up -d`
2. Ingest data: `python ingest_data.py`
