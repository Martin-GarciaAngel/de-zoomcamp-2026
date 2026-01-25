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
3. Ingest data: `python ingest_zones.py`

# Questions

## Question 1
```bash
docker run -it --rm python:3.13-slim pip --version
```

## Question 2
Answer is `db:5432` because pgadmin would connect to the container port since it is running inside the docker network.

## Question 3
```sql
SELECT 
    SUM(CASE WHEN trip_distance <= 1 THEN 1 ELSE 0 END) AS "1 mile"
FROM green_taxi_data
WHERE lpep_pickup_datetime >= '2025-11-01' 
  AND lpep_dropoff_datetime < '2025-12-01';
```

## Question 4
```sql
SELECT 
    lpep_pickup_datetime::date AS pickup_day,
    MAX(trip_distance) AS max_dist
FROM 
    green_taxi_data
WHERE 
    trip_distance < 100
GROUP BY 
    1
ORDER BY 
    max_dist DESC
LIMIT 1;
```

## Question 5
```sql
SELECT 
    z."Zone", 
    ROUND(SUM(t.total_amount)) AS total_sum
FROM 
    green_taxi_data t
JOIN 
    zones z ON t."PULocationID" = z."LocationID"
WHERE 
    t.lpep_pickup_datetime::date = '2025-11-18'  -- Double check if your HW asks for Oct or Nov
GROUP BY 
    z."Zone"
ORDER BY 
    total_sum DESC;
```

## Question 6
```sql
SELECT
    zdrop."Zone" AS dropoff_zone,
    MAX(t.tip_amount) AS max_tip
FROM
    green_taxi_data t
JOIN zones zpick 
    ON t."PULocationID" = zpick."LocationID"
JOIN zones zdrop 
    ON t."DOLocationID" = zdrop."LocationID"
WHERE
    zpick."Zone" = 'East Harlem North' -- Replace with the zone mentioned in your HW
    AND t.lpep_pickup_datetime >= '2025-11-01'
    AND t.lpep_pickup_datetime < '2025-12-01'
GROUP BY
    1
ORDER BY
    max_tip DESC
LIMIT 1;
```

## Question 7
* `terraform init`: Does the initial setup for the backend
* `terraform apply -auto-approve`: Tells terraform to go ahead and build and generates the proposed changes for the plan internally
* `terraform destroy`: Does all the cleanup
