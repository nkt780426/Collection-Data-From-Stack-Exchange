from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType

# Import UDFs from preprocess.py
import preprocess

# Kafka settings
kafka_topic_name = "stack_exchange"
kafka_bootstrap_servers = "localhost:39092"

# Initialize Spark Session with package configurations
spark = SparkSession.builder.appName("KafkaConsumer").getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Define schema for the data
schema = StructType(
    [
        StructField("title", StringType(), True),
        StructField("content", StringType(), True),
        StructField("time", StringType(), True),
        StructField("category", StringType(), True),
        StructField("views", StringType(), True),
        StructField("num_answer", StringType(), True),
        StructField("votes", StringType(), True),
        StructField("solved", StringType(), True),
    ]
)

# Read data from Kafka
df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers)
    .option("subscribe", kafka_topic_name)
    .option("startingOffsets", "latest")
    .load()
)

# Convert JSON data from Kafka to DataFrame and apply preprocessing
df_json = (
    df.selectExpr("CAST(value AS STRING)")
    .select(from_json(col("value"), schema).alias("data"))
    .select("data.*")
    .withColumn("content", preprocess.process_html("content"))
    .withColumn("views", preprocess.convert_to_numeric("views"))
    .withColumn("num_answer", preprocess.convert_to_numeric("num_answer"))
    .withColumn("votes", preprocess.convert_to_numeric("votes"))
)

# Write data to a JSON file
query = (
    df_json.writeStream.outputMode("append")
    .format("json")
    .option("checkpointLocation", "./output/checkpoint")
    .option("path", "./output/data")
    .start()
)

# Wait for the query to finish
query.awaitTermination()
