from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("KafkaStructuredStreaming") \
    .getOrCreate()

# Define the Kafka broker and topic
kafkaBrokers = "localhost:9092"
topic = "my-topic"

# Read data from Kafka as a streaming DataFrame
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafkaBrokers) \
    .option("subscribe", topic) \
    .load()

# Perform operations on the streaming DataFrame
# For example, you can select specific columns or apply filters

# Write the processed data to an output sink (e.g., console or file)
outputQuery = df.writeStream \
    .format("console") \
    .start()

# Wait for the stream processing to finish
outputQuery.awaitTermination()
