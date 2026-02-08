# Data Engineering Zoomcamp 2026 - Module 1

This repository contains my homework submissions for the first module of the DE Zoomcamp.

## setup
1. Start the infrastructure: `load_yellow_taxi.py`

```sql
CREATE OR REPLACE EXTERNAL TABLE `steel-bliss-486723-d9.yellow_ny_taxi_2024.external_yellow_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://dezoomcamp_hw3_2026_martin_ga/yellow_tripdata_2024-*.parquet']
);


CREATE OR REPLACE TABLE `steel-bliss-486723-d9.yellow_ny_taxi_2024.yellow_tripdata_2024` AS
SELECT * FROM `steel-bliss-486723-d9.yellow_ny_taxi_2024.external_yellow_tripdata`;
```

# Questions

## Question 1
```sql
SELECT count(*) 
FROM `steel-bliss-486723-d9.yellow_ny_taxi_2024.yellow_tripdata_2024`
```

## Question 2
```sql
SELECT COUNT(DISTINCT(PULocationID)) FROM `steel-bliss-486723-d9.yellow_ny_taxi_2024.external_yellow_tripdata`;

SELECT COUNT(DISTINCT(PULocationID)) FROM `steel-bliss-486723-d9.yellow_ny_taxi_2024.yellow_tripdata_2024`;

```

## Question 3

```sql
SELECT PULocationID 
FROM `steel-bliss-486723-d9.yellow_ny_taxi_2024.yellow_tripdata_2024`

SELECT PULocationID, DOLocationID 
FROM `steel-bliss-486723-d9.yellow_ny_taxi_2024.yellow_tripdata_2024`;
```

## Question 4
```sql
SELECT count(*) 
FROM `steel-bliss-486723-d9.yellow_ny_taxi_2024.yellow_tripdata_2024`
WHERE fare_amount = 0;
```

## Question 5
```sql
CREATE OR REPLACE TABLE `steel-bliss-486723-d9.yellow_ny_taxi_2024.yellow_tripdata_2024_partitioned_clustered`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `steel-bliss-486723-d9.yellow_ny_taxi_2024.external_yellow_tripdata`;
```

## Question 6
```sql
SELECT DISTINCT(VendorID)
FROM `steel-bliss-486723-d9.yellow_ny_taxi_2024.yellow_tripdata_2024_partitioned_clustered`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

SELECT DISTINCT(VendorID)
FROM `steel-bliss-486723-d9.yellow_ny_taxi_2024.yellow_tripdata_2024`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';
```