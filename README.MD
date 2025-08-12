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

All services are designed to work together seamlessly through shared configurations and a common network. This diagram illustrates the flow of data from ingestion to analytics.

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

<table>
  <thead>
    <tr>
      <th align="left">Component</th>
      <th align="left">Role and Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>NiFi</strong></td>
      <td><strong>Data Orchestration & Ingestion</strong>. Think of NiFi as a smart, visual postal service for your data. It picks up data from various sources, allows you to visually route and modify it, and then reliably delivers it to HDFS.</td>
    </tr>
    <tr>
      <td><strong>Hadoop HDFS</strong></td>
      <td><strong>Durable Storage Layer</strong>. This is like a giant, infinitely expandable, and super-reliable hard drive for all your data. It's the "single source of truth" where both raw and processed data are stored safely.</td>
    </tr>
    <tr>
      <td><strong>Hive Metastore</strong></td>
      <td><strong>Central Metadata Catalog</strong>. If HDFS is a library of books, the Metastore is the card catalog. It doesn't hold the actual data, but it holds all the information *about* the data, making it easy for tools like Spark and Trino to find and understand it.</td>
    </tr>
    <tr>
      <td><strong>Spark</strong></td>
      <td><strong>Transformation & Processing Engine</strong>. This is the pipeline's heavy-duty workshop. Spark takes the raw data, applies complex transformations, and produces valuable, structured datasets ready for analysis.</td>
    </tr>
    <tr>
      <td><strong>Trino</strong></td>
      <td><strong>Distributed SQL Query Engine</strong>. Trino is the universal translator for your data. It lets you use standard SQL to ask complex questions of your data, whether it lives in HDFS or another data source.</td>
    </tr>
    <tr>
      <td><strong>Superset</strong></td>
      <td><strong>Business Intelligence & Visualization</strong>. This is the showroom for your data. Superset connects to Trino and turns the queried data into easy-to-understand charts, graphs, and interactive dashboards.</td>
    </tr>
    <tr>
      <td><strong>Prometheus</strong></td>
      <td><strong>Metrics Collection System</strong>. Think of Prometheus as a diligent security guard who constantly patrols the pipeline, taking detailed notes (metrics) on how every component is performing.</td>
    </tr>
  </tbody>
</table>

---
## ⛓️ Component Repositories

The configuration for each component is maintained in its own dedicated repository. This main repository contains the `docker-compose.yml` to orchestrate them all.

| Component                 | Repository Link                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| 🐘 **Hadoop** | [unspokenmyth/hadoop_conf](https://github.com/unspokenmyth/hadoop_conf)                  |
| 🐝 **Hive** | [unspokenmyth/hive_conf](https://github.com/unspokenmyth/hive_conf)                      |
| 🌊 **NiFi** | [unspokenmyth/nifi_conf](https://github.com/unspokenmyth/nifi_conf)                      |
| ✨ **Spark** | [unspokenmyth/spark_build](https://github.com/unspokenmyth/spark_build)                  |
| 🔌 **Trino** | [unspokenmyth/trino_configs](https://github.com/unspokenmyth/trino_configs)              |
| 📊 **Prometheus** | [unspokenmyth/prometheus_config](https://github.com/unspokenmyth/prometheus_config)      |
| 📈 **Superset** | [unspokenmyth/superset_config](https://github.com/unspokenmyth/superset_config)          |

### Quick Clone

To get all the repositories on your local machine, run the following commands:

```bash
git clone [https://github.com/unspokenmyth/hadoop_conf.git](https://github.com/unspokenmyth/hadoop_conf.git)
git clone [https://github.com/unspokenmyth/hive_conf.git](https://github.com/unspokenmyth/hive_conf.git)
git clone [https://github.com/unspokenmyth/nifi_conf.git](https://github.com/unspokenmyth/nifi_conf.git)
git clone [https://github.com/unspokenmyth/spark_build.git](https://github.com/unspokenmyth/spark_build.git)
git clone [https://github.com/unspokenmyth/trino_configs.git](https://github.com/unspokenmyth/trino_configs.git)
git clone [https://github.com/unspokenmyth/prometheus_config.git](https://github.com/unspokenmyth/prometheus_config.git)
git clone [https://github.com/unspokenmyth/superset_config.git](https://github.com/unspokenmyth/superset_config.git)
```
