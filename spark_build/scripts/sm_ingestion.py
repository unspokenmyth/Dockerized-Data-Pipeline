from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
import random
import string

# Enhanced SparkSession with Hive support
spark = SparkSession.builder \
    .appName("social_media_monitoring_hudi") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .config("spark.sql.hive.convertMetastoreParquet", "false") \
    .config("spark.sql.extensions", "org.apache.spark.sql.hudi.HoodieSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.hudi.catalog.HoodieCatalog") \
    .config("spark.hadoop.hive.metastore.uris", "thrift://hive-metastore:9083") \
    .enableHiveSupport() \
    .getOrCreate()

# Ensure database exists
spark.sql("CREATE DATABASE IF NOT EXISTS hive_db")

# Generate dummy data
data = []
for i in range(50):
    data.append((
        i,
        ''.join(random.choices(string.ascii_lowercase, k=8)),
        random.choice(['twitter', 'facebook', 'instagram']),
        random.randint(0, 500),
        random.randint(0, 100),
        random.randint(0, 1000),
        '2025-07-17'
    ))

columns = ['id', 'username', 'platform', 'likes', 'comments', 'shares', 'date']
df = spark.createDataFrame(data, schema=columns)

base_path = "hdfs://namenode:9000/user/hive/warehouse/hive_db.db/social_media_monitoring_data"

# Write with enhanced Hive sync options
df.write.format("hudi") \
    .option("hoodie.table.name", "social_media_monitoring_data") \
    .option("hoodie.datasource.write.recordkey.field", "id") \
    .option("hoodie.datasource.write.precombine.field", "date") \
    .option("hoodie.datasource.write.table.type", "COPY_ON_WRITE") \
    .option("hoodie.datasource.hive_sync.enable", "true") \
    .option("hoodie.datasource.hive_sync.database", "hive_db") \
    .option("hoodie.datasource.hive_sync.table", "social_media_monitoring_data") \
    .option("hoodie.datasource.hive_sync.metastore.uris", "thrift://hive-metastore:9083") \
    .option("hoodie.datasource.hive_sync.use_jdbc", "false") \
    .option("hoodie.datasource.hive_sync.mode", "hms") \
    .option("hoodie.datasource.hive_sync.support_timestamp", "true") \
    .option("hoodie.datasource.hive_sync.partition_fields", "") \
    .mode("overwrite") \
    .save(base_path)

spark.stop()

