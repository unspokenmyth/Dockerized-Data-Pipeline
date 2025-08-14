# 🚀 Open-Source Data Pipeline

This repository provides a complete, containerized data pipeline built entirely from open-source components. It's designed to provide a reproducible, production-inspired environment for high-speed data ingestion, transformation, and querying, all without vendor lock-in.

This project is ideal for data engineers, platform engineers, and developers looking for a powerful, local-first data environment that can be scaled to production.

---

## ✨ Key Goals

* **Accelerated Workflow**: Move from raw data to actionable insight faster with efficient, incremental pipelines and a high-speed query layer.
* **Reproducible Environments**: Eliminate "it works on my machine" issues with versioned configurations and containerized services.
* **Open & Interoperable**: Build on a foundation of open standards and APIs, ensuring easy integration with any tool.
* **Observable by Default**: Integrated monitoring provides immediate visibility into performance and system health.

---

## 🏗️ Pipeline Architecture

All services are orchestrated via Docker Compose to work together seamlessly through a shared network. This diagram illustrates the flow of data from ingestion to analytics.

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
        (Superset, Prometheus)
      </td>
    </tr>
  </tbody>
</table>

---

## 🧩 Core Components & Their Roles

The configuration for each component is maintained in its own dedicated repository and included here as a Git submodule. This main repository contains the `docker-compose.yml` to orchestrate them all.

| Component                                                                    | Description                                                    |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 🐘 [**Hadoop**](https://github.com/unspokenmyth/hadoop_conf)                   | Durable, distributed file system for scalable data storage.    |
| 🐝 [**Hive**](https://github.com/unspokenmyth/hive_conf)                       | Central metastore service for managing the data catalog.       |
| 🌊 [**NiFi**](https://github.com/unspokenmyth/nifi_conf)                       | Visual tool for orchestrating data flow and ingestion.         |
| ✨ [**Spark**](https://github.com/unspokenmyth/spark_build)                    | Engine for large-scale data processing and transformation.     |
| 🔌 [**Trino**](https://github.com/unspokenmyth/trino_configs)                  | Fast, distributed SQL query engine for federated analytics.    |
| 📊 [**Prometheus**](https://github.com/unspokenmyth/prometheus_config)        | System for monitoring services and collecting metrics.         |
| 📈 [**Superset**](https://github.com/unspokenmyth/superset_config)             | Platform for data exploration, visualization, and dashboards.  |

---

## 🚀 Getting Started

Follow these steps to get the entire data pipeline running on your local machine.

### Prerequisites

* **Docker** and **Docker Compose**
* **Git**

### Installation & Launch

1.  **Clone the Repository with Submodules**

    Clone this repository. The `--recurse-submodules` flag is important as it will also clone all the necessary configuration repositories.

    ```bash
    git clone --recurse-submodules [https://github.com/unspokenmyth/open-data-pipeline.git](https://github.com/unspokenmyth/open-data-pipeline.git)
    cd open-data-pipeline
    ```
    *(Note: Replace the URL with your actual repository URL.)*

2.  **Launch the Pipeline**

    Use Docker Compose to build the images and start all the services in the background.

    ```bash
    docker-compose up -d
    ```

3.  **Verify the Services**

    Check the status of the running containers to ensure everything started correctly.

    ```bash
    docker-compose ps
    ```

    You should see all services listed with a `running` or `healthy` state. It may take a few minutes for all services to initialize fully.

### Accessing Services

Once the stack is running, you can access the various web UIs:

| Service    | URL                           |
| ---------- | ----------------------------- |
| **NiFi** | `http://localhost:8080/nifi`  |
| **Superset** | `http://localhost:8088`       |
| **Prometheus** | `http://localhost:9090`       |
| **HDFS UI** | `http://localhost:9870`       |

### Shutting Down

To stop and remove all the running containers, network, and volumes, run the following command from your project directory:

```bash
docker-compose down
```
