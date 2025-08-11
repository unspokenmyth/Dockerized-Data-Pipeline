# Open-Source Data Pipeline

This repository provides a complete, containerized data pipeline built entirely from open-source components. It's designed to provide a reproducible, production-inspired environment for high-speed data ingestion, transformation, and querying, all without vendor lock-in.

This project is ideal for data engineers, platform engineers, and developers looking for a powerful, local-first data environment that can be scaled to production.

---

### Quick Start

For experienced users, here are the essential steps to get the pipeline running:

    # 1. Clone the repository
    git clone <your-repo-url>
    cd <repo-name>

    # 2. Create your environment file from the example
    cp .env.example .env

    # 3. Launch the stack
    docker compose up -d --build

Access services at their respective ports (e.g., Superset at http://localhost:8088).

---

## Key Goals

* **Accelerated Workflow**: Move from raw data to actionable insight faster with efficient, incremental pipelines and a high-speed query layer.
* **Reproducible Environments**: Eliminate "it works on my machine" issues with versioned configurations and containerized services.
* **Open & Interoperable**: Build on a foundation of open standards and APIs, ensuring easy integration with any tool.
* **Observable by Default**: Integrated monitoring provides immediate visibility into performance and system health.

---

## Pipeline Architecture

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
        (Spark, Ignite, Trino)
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

## Core Components & Their Roles

<table>
  <thead>
    <tr>
      <th align="left">Component</th>
      <th align="left">Role and Explanation</th>
      <th align="left">Documentation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>NiFi</strong></td>
      <td><strong>Data Orchestration & Ingestion</strong>. Think of NiFi as a smart, visual postal service for your data. It picks up data from various sources, allows you to visually route and modify it, and then reliably delivers it to HDFS.</td>
      <td><a href="https://nifi.apache.org/docs.html">Official Docs</a></td>
    </tr>
    <tr>
      <td><strong>Hadoop HDFS</strong></td>
      <td><strong>Durable Storage Layer</strong>. This is like a giant, infinitely expandable, and super-reliable hard drive for all your data. It's the "single source of truth" where both raw and processed data are stored safely.</td>
      <td><a href="https://hadoop.apache.org/docs/current/">Official Docs</a></td>
    </tr>
    <tr>
      <td><strong>Hive Metastore</strong></td>
      <td><strong>Central Metadata Catalog</strong>. If HDFS is a library of books, the Metastore is the card catalog. It doesn't hold the actual data, but it holds all the information *about* the data, making it easy for tools like Spark and Trino to find and understand it.</td>
      <td><a href="https://cwiki.apache.org/confluence/display/hive">Official Docs</a></td>
    </tr>
    <tr>
      <td><strong>Spark</strong></td>
      <td><strong>Transformation & Processing Engine</strong>. This is the pipeline's heavy-duty workshop. Spark takes the raw data, applies complex transformations, and produces valuable, structured datasets ready for analysis.</td>
      <td><a href="https://spark.apache.org/docs/latest/">Official Docs</a></td>
    </tr>
    <tr>
      <td><strong>Ignite</strong></td>
      <td><strong>In-Memory Speed Layer</strong>. Think of Ignite as a high-speed cache or a "shortcut" for your most frequently accessed data. By keeping important data in RAM, it allows Trino to retrieve answers for certain queries almost instantly.</td>
      <td><a href="https://ignite.apache.org/docs/latest/">Official Docs</a></td>
    </tr>
    <tr>
      <td><strong>Trino</strong></td>
      <td><strong>Distributed SQL Query Engine</strong>. Trino is the universal translator for your data. It lets you use standard SQL to ask complex questions of your data, whether it lives in HDFS or the high-speed Ignite cache.</td>
      <td><a href="https://trino.io/docs/current/">Official Docs</a></td>
    </tr>
    <tr>
      <td><strong>Superset</strong></td>
      <td><strong>Business Intelligence & Visualization</strong>. This is the showroom for your data. Superset connects to Trino and turns the queried data into easy-to-understand charts, graphs, and interactive dashboards.</td>
      <td><a href="https://superset.apache.org/docs/intro">Official Docs</a></td>
    </tr>
    <tr>
      <td><strong>Prometheus</strong></td>
      <td><strong>Metrics Collection System</strong>. Think of Prometheus as a diligent security guard who constantly patrols the pipeline, taking detailed notes (metrics) on how every component is performing.</td>
      <td><a href="https://prometheus.io/docs/introduction/overview/">Official Docs</a></td>
    </tr>
    <tr>
      <td><strong>Grafana</strong></td>
      <td><strong>Monitoring & Observability Dashboard</strong>. Grafana is the central monitoring room where all of Prometheus's notes are displayed on easy-to-read screens, graphs, and alerts.</td>
      <td><a href="https://grafana.com/docs/grafana/latest/">Official Docs</a></td>
    </tr>
  </tbody>
</table>

---

## Getting Started (Local Development)

This section provides a detailed guide to setting up and running the data pipeline on your local machine.

### 1. Prerequisites

Before you begin, ensure you have the following installed and configured:

* **Git**: For cloning the repository.
* **Docker & Docker Compose**: The core engine for running the containerized services.
* **System Resources**: It is highly recommended to allocate at least **12GB of RAM** to Docker for stable performance across all services.
* **Configuration Folders**: Confirm all configuration folders (*nifi_conf*, *hadoop_conf*, etc.) are present in the project root.

### 2. Environment Setup

This project uses an *.env* file to manage secrets and environment-specific variables. You must create this file before starting the services.

1.  Navigate to the root of the project directory in your terminal.
2.  Copy the example environment file to create your own local version:

        cp .env.example .env

3.  **Important**: Open the new *.env* file in a text editor. While the defaults will work for a quick start, it is best practice to **change the default secrets** like *SUPERSET_SECRET_KEY* for better security, even in a local environment.

### 3. Launch the Pipeline

With the prerequisites and environment file in place, you can launch the entire pipeline with a single command:

    docker compose up -d --build

* **What this command does:**
    * *docker compose up*: Starts all services defined in the *docker-compose.yml* file.
    * *-d*: Runs the containers in "detached mode" in the background.
    * *--build*: Builds the custom Spark image from the *spark_build* directory if it doesn't already exist.

The first run will take several minutes to download all the necessary container images. Subsequent starts will be much faster.

### 4. Verify the Setup (Optional)

You can check the logs to see the services starting up and ensure everything is healthy:

    # View the logs for all services in real-time
    docker compose logs -f

    # Press Ctrl+C to exit the log view.

Once the services are up, you can also test HDFS connectivity directly:

    # List the root directory of HDFS
    docker compose exec namenode hdfs dfs -ls /

### 5. Access Service Endpoints

Once all services are healthy, you can access their web interfaces:

<table>
  <thead>
    <tr>
      <th align="left">Service</th>
      <th align="left">URL</th>
      <th align="left">Credentials</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>NiFi</strong></td>
      <td>http://localhost:8080/nifi</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Trino</strong></td>
      <td>http://localhost:8080</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Superset</strong></td>
      <td>http://localhost:8088</td>
      <td>admin / admin</td>
    </tr>
    <tr>
      <td><strong>Grafana</strong></td>
      <td>http://localhost:3000</td>
      <td>admin / admin</td>
    </tr>
    <tr>
      <td><strong>Prometheus</strong></td>
      <td>http://localhost:9090</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>HDFS UI</strong></td>
      <td>http://localhost:9870</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Spark App UI</strong></td>
      <td>http://localhost:4040</td>
      <td><em>Visible only when a Spark job is running</em></td>
    </tr>
  </tbody>
</table>


### 6. Stopping the Pipeline

* **To stop all running containers** without losing your data:

        docker compose down

* **To stop containers AND permanently delete all persistent data** (HDFS files, databases, etc.), use the *-v* flag. This is useful for a clean restart.

        docker compose down -v

---

## A Typical Workflow in Action

The end-to-end process follows these four main stages: Ingest, Transform, Query, and Visualize.

1.  **Ingest Data**: Open the **NiFi UI**. A simple flow could be *GetFile* -> *SplitText* -> *PutHDFS*. Configure *PutHDFS* to write to a path like */raw/my_data*.
2.  **Transform It**: Execute a Spark job to process the raw data. This job would read from */raw/my_data*, apply business logic (e.g., clean, filter, aggregate), and write the result into a partitioned Hudi table in a curated path like */curated/my_table*.

        # Enter the Spark container's shell
        docker compose exec spark /bin/bash

        # Submit the job from within the container
        spark-submit \
          --class com.example.MyJob \
          --master local[*] \
          /opt/spark/jobs/your_transform_job.jar

3.  **Query Instantly**: The Spark job should have registered the table in the Hive Metastore. Now you can query it immediately from Trino.

        -- Discover tables in the 'curated' schema
        SHOW TABLES FROM hive.curated;

        -- Run an analytical query
        SELECT category, COUNT(*) as event_count
        FROM hive.curated.my_table
        GROUP BY category
        ORDER BY event_count DESC;

4.  **Visualize Insights**: In **Superset**, go to **Data -> Databases**, add a new database connection for Trino, then go to **Data -> Datasets** to add your new table. You can then create charts and dashboards.

---

## Configuration & Customization

The power of this pipeline lies in its shared, version-controlled configurations.

* *hadoop_conf/*: Shared HDFS client settings (*fs.defaultFS*) used by all services.
* *hive_conf/*: Central *hive-site.xml* defining the Metastore connection.
* *nifi_conf/*: Configurations specific to NiFi, including Hadoop client overrides.
* *prometheus/*: *prometheus.yml* scrape configs and alert rules.
* *spark_build/*: *Dockerfile* for the custom Spark runtime. Add job dependencies here.
* *trino_plugins/*: Trino server settings, JVM tuning, and catalog property files.

### Understanding Trino JMX Metrics

This section explains how Prometheus collects metrics from Trino.

* **How it Works**: The Trino service is configured with a Prometheus JMX agent. This agent starts a lightweight web server inside the Trino container on a specific port (e.g., 7071) and exposes all of Trino's internal metrics at a */metrics* URL.
* **Prometheus's Role**: The main Prometheus container is configured in *prometheus.yml* to periodically visit that URL (*trino:7071/metrics*) and scrape (save) the metrics it finds there.
* **Key Takeaway**: This setup allows for detailed monitoring of Trino's query performance, memory usage, and overall health without the complexity of traditional JMX connections.

---

## Troubleshooting

* **Problem: HDFS Write Failures**
    * **Solution 1**: Ensure every Hadoop-aware service (NiFi, Spark, Trino) uses the exact same *fs.defaultFS=hdfs://namenode:9000*. Note that *9000* is the RPC port, not the *9870* Web UI port.
    * **Solution 2**: For development, ensure *dfs.replication=1* is set in your *hdfs-site.xml* to prevent under-replication errors on a single-node cluster.

* **Problem: Trino Can’t See Tables**
    * **Solution 1**: Confirm the Hive Metastore is accessible from the Trino container at *thrift://hive-metastore:9083*.
    * **Solution 2**: Verify that your Spark/Hudi job successfully synced the table and partition metadata to the Metastore upon completion.
    * **Solution 3**: Ensure Trino’s Hive catalog properties (*trino_plugins/catalog/hive.properties*) include a line like *hive.config.resources=/etc/hadoop/core-site.xml,/etc/hadoop/hdfs-site.xml* so it knows how to connect to HDFS.

* **Problem: Prometheus Target for Trino is DOWN**
    * **Solution**: In your *prometheus.yml*, use the target *trino:7071* for direct container-to-container scraping. The target *host.docker.internal* is a special DNS name for Docker Desktop and will not work in other Docker environments.

* **Problem: NiFi UI Not Reachable on 8080**
    * **Solution**: Check your *docker-compose.yml* to see which host port NiFi is mapped to. If another service like Trino is using port *8080*, NiFi might be mapped to a different one. Also, verify the *nifi.web.http.port* in your *nifi.properties* file.

---

## Production Readiness Checklist

* **Security**:
    * **Crucially, change the default *admin/admin* credentials for Superset and Grafana immediately upon first login.**
    * Replace all default secrets in your *.env* file with strong, managed credentials. Use a proper secrets management system like Vault or AWS Secrets Manager.
    * Enable authentication and TLS on all public-facing endpoints (Trino, Superset, NiFi).

* **Data Durability**:
    * Increase HDFS replication factor from `1` to `3` or more in *hadoop_conf/hdfs-site.xml*.
    * Use a production-grade managed database for the Hive Metastore and Superset backends.

* **Permissions**:
    * Enable HDFS permissions in *hadoop_conf/hdfs-site.xml* and configure appropriate access control lists (ACLs).

---

## Contributing

Contributions are welcome and greatly appreciated! You can contribute in several ways:

* **Improve Documentation**: Fix typos, clarify instructions, or add new sections.
* **Add Dashboards**: Contribute pre-built Grafana dashboard JSON models for monitoring different components.
* **Submit Job Examples**: Add new Spark job examples to the repository to showcase different transformation patterns.
* **Enhance Deployment**: Create or improve deployment templates for other environments like Kubernetes.

Please keep configurations sanitized and do not commit secrets to the repository.

## License

All software components included in this project are open source and are governed by their own respective licenses.