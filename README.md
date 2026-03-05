# Stripe Data Pipeline Demo

## Overview

This project demonstrates a **real-time data pipeline** inspired by a payment platform architecture (similar to Stripe).

Transactions are simulated by a Python producer, streamed through **Apache Kafka**, processed by a consumer service, and stored in **MongoDB** as a feature store for fraud detection.

This project was developed as part of the **RNCP Level 7 – AI Architect certification (Bloc 2: AI Data Architecture)**.

---

## Architecture

The architecture follows a simplified real-time data platform:

Stripe Applications
↓
PostgreSQL (OLTP)
↓
CDC – Debezium
↓
Apache Kafka (Event Streaming)

Two processing paths:

**Real-time path**
Kafka → Consumer → MongoDB (Feature Store)

**Analytics path**
Kafka → Data Lake → Data Warehouse → BI Analytics

In this demo implementation, the following components are deployed locally using Docker:

* Apache Kafka
* Zookeeper
* PostgreSQL
* MongoDB

---

## Pipeline Flow

1. A **Python producer** simulates payment transactions.
2. Transactions are sent to a **Kafka topic**.
3. A **consumer service** reads the events from Kafka.
4. The processed transactions are stored in **MongoDB**.

This pipeline represents the **real-time fraud detection feature pipeline**.

---

## Technologies Used

* Python
* Apache Kafka
* Docker
* MongoDB
* PostgreSQL
* Docker Compose

---

## Project Structure

```
stripe-data-pipeline-demo
│
├── docker-compose.yml
├── producer.py
├── consumer_mongo.py
│
├── README.md
├── .gitignore
└── LICENSE
```

---

## Running the Pipeline

### Start infrastructure

```
docker-compose up -d
```

This starts:

* Kafka
* Zookeeper
* PostgreSQL
* MongoDB

---

### Run the producer

```
python producer.py
```

This script generates simulated Stripe transactions and publishes them to Kafka.

---

### Run the consumer

```
python consumer_mongo.py
```

This service consumes the Kafka messages and stores them in MongoDB.


