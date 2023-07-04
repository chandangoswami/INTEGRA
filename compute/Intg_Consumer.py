from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import col,from_json

# Define the Kafka broker and topic
kafkaBrokers = "BRO1:9092"
topic = "fe-request"


# Create a SparkSession
spark = SparkSession.builder \
    .appName("IntegraConsumer") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel('WARN')

# Read data from Kafka as a streaming DataFrame
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafkaBrokers) \
    .option("subscribe", topic) \
    .load()


df1 = (df_raw
    .withColumn("key", df_raw["key"].cast(StringType()))
    .withColumn("value", df_raw["value"].cast(StringType()))
    )

dfJSON = df1.select("value")

flow_schema =  StructType ([
StructField("wfName",StringType(),True),
StructField("wfType",StringType(),True),
StructField("wfId",StringType(),True),
StructField("ver",StringType(),True),
StructField("create_date",StringType(),True),
StructField("modified_date",StringType(),True),
StructField("trigger",StringType(),True) 
]) 

dfJ = dfJSON.withColumn("jsonData",from_json(col("value"),flow_schema)).select("jsonData.*")

query = df1.select("value")  \
    .writeStream \
    .outputMode("append")\
    .option("multiline","true")\
    .format("console") \
    .start()

# Wait for the stream processing to finish
query.awaitTermination()
