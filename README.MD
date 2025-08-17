# 🚀 Dockerized Open-Source Data Pipeline

Welcome! This repository contains a fully containerized, open-source data pipeline designed for learning, development, and production use. At its core is a single **`docker-compose.yml`** file that orchestrates the entire stack, allowing you to launch a complete data platform with one command.

Whether you're exploring data engineering or building a robust data infrastructure, this project provides a powerful and reproducible environment.

---

## ✨ Features

* **One-Command Setup**: Launch the entire multi-service pipeline with a single `docker-compose up` command.
* **100% Open-Source**: Built entirely on trusted, community-driven projects with no vendor lock-in.
* **Production Inspired**: The architecture mirrors real-world data platforms, providing a practical learning environment.
* **Built-in Monitoring**: Integrated Prometheus and Grafana provide immediate visibility into the health and performance of your pipeline.

---

## 🏗️ Architecture Overview

The pipeline is designed as a series of stages, with data flowing from ingestion to analytics. All services are defined and linked within the `docker-compose.yml` file, creating a seamless, networked environment right out of the box.


<table>
  <tbody>
    <tr>
      <td align="center" style="padding: 10px; border: 1px solid #666; background-color: #f2f2f2; border-radius: 8px;">
        <b>Stage 1: Ingestion</b><br>
        (NiFi)
      </td>
    </tr>
    <tr><td align="center" style="font-size: 24px; line-height: 0.5;">&darr;</td></tr>
    <tr>
      <td align="center" style="padding: 10px; border: 1px solid #666; background-color: #f2f2f2; border-radius: 8px;">
        <b>Stage 2: Storage & Metadata</b><br>
        (Hadoop HDFS, Hive Metastore)
      </td>
    </tr>
    <tr><td align="center" style="font-size: 24px; line-height: 0.5;">&darr;</td></tr>
    <tr>
      <td align="center" style="padding: 10px; border: 1px solid #666; background-color: #f2f2f2; border-radius: 8px;">
        <b>Stage 3: Processing & Query</b><br>
        (Spark, Trino)
      </td>
    </tr>
    <tr><td align="center" style="font-size: 24px; line-height: 0.5;">&darr;</td></tr>
    <tr>
      <td align="center" style="padding: 10px; border: 1px solid #666; background-color: #f2f2f2; border-radius: 8px;">
        <b>Stage 4: Analytics & Observability</b><br>
        (Superset, Prometheus, Grafana)
      </td>
    </tr>
  </tbody>
</table>

---

## 🧩 The Tech Stack

This pipeline integrates best-in-class open-source tools. The configuration for each service is managed in its own repository and included here as a Git submodule.

| Service                                                                      | Role in the Pipeline                                           |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 🐘 [**Hadoop**](https://github.com/unspokenmyth/hadoop_config)                 | Provides distributed, fault-tolerant storage with HDFS.        |
| 🐝 [**Hive**](https://github.com/unspokenmyth/hive_config)                     | Acts as the central metadata catalog for all our data.         |
| 🌊 [**NiFi**](https://github.com/unspokenmyth/nifi_config)                     | Manages data ingestion and automates data flows visually.      |
| ✨ [**Spark**](https://github.com/unspokenmyth/spark_config)                   | Powers large-scale data transformation and processing.         |
| 🔌 [**Trino**](https://github.com/unspokenmyth/trino_config)                   | Enables fast, interactive SQL queries across all data sources. |
| 📊 [**Prometheus**](https://github.com/unspokenmyth/prometheus_config)        | Collects metrics on the health and performance of all services.|
| 📉 [**Grafana**](https://github.com/unspokenmyth/grafana_config)               | Visualizes monitoring data with powerful, interactive dashboards.|
| 📈 [**Superset**](https://github.com/unspokenmyth/superset_config)             | Provides data exploration, visualization, and BI dashboards.   |


---

## 🚀 Getting Started

Ready to launch? Follow these simple steps.

### Prerequisites
* **Docker** and **Docker Compose**
* **Git**

### Installation
1.  **Clone This Repository**

    Use the `--recurse-submodules` flag to ensure the configuration for all services is downloaded correctly.

    ```bash
    git clone --recurse-submodules [https://github.com/unspokenmyth/dockerized-data-pipeline.git](https://github.com/unspokenmyth/dockerized-data-pipeline.git)
    cd dockerized-data-pipeline
    ```

2.  **Launch the Pipeline**

    This single command will download, build, and start all services in the background. Please be patient, as the initial startup can take several minutes.

    ```bash
    docker-compose up -d
    ```

3.  **Access the Services**

    Once the services are running, you can access their web interfaces:

    | Service      | URL                           |
    |--------------|-------------------------------|
    | **NiFi** | `http://localhost:8080/nifi`  |
    | **Superset** | `http://localhost:8088`       |
    | **Prometheus**| `http://localhost:9090`       |
    | **Grafana** | `http://localhost:3000`       |
    | **HDFS UI** | `http://localhost:9870`       |

---

## ⚙️ Managing the Pipeline

Here are some useful commands to manage your running environment.

* **Check Status**: To see the status of all running containers, use:
    ```bash
    docker-compose ps
    ```
* **Stop the Pipeline**: To stop and remove all containers, networks, and volumes, use:
    ```bash
    docker-compose down
    ```
