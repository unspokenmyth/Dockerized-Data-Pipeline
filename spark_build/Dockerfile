FROM openjdk:11-jdk-slim

ENV SPARK_VERSION=3.3.4 \
    HADOOP_VERSION=3 \
    SPARK_HOME=/opt/spark \
    JAVA_HOME=/usr/local/openjdk-11 \
    PYTHONPATH=${SPARK_HOME}/python:${SPARK_HOME}/python/lib/py4j-*.zip:$PYTHONPATH \
    PATH=${SPARK_HOME}/bin:${SPARK_HOME}/sbin:${PATH}

# Install system packages
RUN apt-get update && apt-get install -y \
    curl wget bash tar procps python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Link python3 to python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Create directories
RUN mkdir -p /opt/spark /data

# Copy and extract Spark
COPY spark-3.3.4-bin-hadoop3.tgz /tmp/
RUN tar -xzf /tmp/spark-3.3.4-bin-hadoop3.tgz -C /tmp && \
    mv /tmp/spark-3.3.4-bin-hadoop3/* ${SPARK_HOME}/ && \
    rm -rf /tmp/spark-3.3.4-bin-hadoop3 /tmp/spark-3.3.4-bin-hadoop3.tgz && \
    ls -l ${SPARK_HOME}/jars | wc -l

# Add Hudi-Spark bundle
RUN wget -q -O /opt/spark/jars/hudi-spark3.3-bundle_2.12-0.13.1.jar \
    https://repo1.maven.org/maven2/org/apache/hudi/hudi-spark3.3-bundle_2.12/0.13.1/hudi-spark3.3-bundle_2.12-0.13.1.jar

# Fix permissions
RUN chown -R root:root /opt/spark && chmod -R 755 /opt/spark

# Fix hardcoded paths in Spark scripts
RUN find ${SPARK_HOME}/bin -type f -exec sed -i 's|/opt/spark-3.3.4-bin-hadoop3|/opt/spark|g' {} \; && \
    find ${SPARK_HOME}/sbin -type f -exec sed -i 's|/opt/spark-3.3.4-bin-hadoop3|/opt/spark|g' {} \;

# Create Spark configuration for Hudi
RUN echo 'spark.sql.extensions=org.apache.spark.sql.hudi.HoodieSparkSessionExtension\n\
spark.sql.catalog.spark_catalog=org.apache.spark.sql.hudi.catalog.HoodieCatalog\n\
spark.sql.adaptive.enabled=true\n\
spark.sql.adaptive.coalescePartitions.enabled=true' > ${SPARK_HOME}/conf/spark-defaults.conf

WORKDIR /opt/spark

# Expose Spark ports
EXPOSE 8080 8081 4040 18080

CMD ["/bin/bash"]



