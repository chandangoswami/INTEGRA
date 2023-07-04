from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
    .appName("KafkaJsonStreaming") \
    .getOrCreate()

# Read data from Kafka topic as a DataFrame
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "BRO1:9092") \
    .option("subscribe", "fe-request") \
    .load()

# Convert value column from binary to string
json_df = kafka_df.selectExpr("CAST(value AS STRING)")

# Parse JSON strings into a structured DataFrame
parsed_df = spark.read\
    .json(json_df.rdd.map(lambda row: row.value))

# Write the parsed DataFrame to the console
query = parsed_df.writeStream \
    .format("console") \
    .start()

# Wait for the query to terminate
query.awaitTermination()
