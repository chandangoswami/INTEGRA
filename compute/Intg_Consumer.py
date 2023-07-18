from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import col,from_json

from util.getSparkSession import getSparkSession

# Define the Kafka broker and topic
kafkaBrokers = "BRO1:9092"
topic = "fe-request"

def main(kafkaBrokers, topic):
    
    spark = getSparkSession()

    # Read data from Kafka as a streaming DataFrame
    df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafkaBrokers) \
    .option("subscribe", topic) \
    .load()


    flow_schema =  StructType ([
    StructField("wfName",StringType(),True),
    StructField("wfType",StringType(),True),
    StructField("wfId",StringType(),True),
    StructField("ver",StringType(),True),
    StructField("create_date",StringType(),True),
    StructField("modified_date",StringType(),True),
    StructField("trigger",StringType(),True) 
    ]) 

    df_casted = (df_raw
    .withColumn("key", df_raw["key"].cast(StringType()))
    .withColumn("value", df_raw["value"].cast(StringType()))
    ).select('value').withColumn("jsonData",from_json(col("value"),flow_schema)).select("jsonData.*") 

    print("Column name : ")
    print(df_casted.columns)

    query = df_casted.select(['wfName', 'wfType', 'wfId', 'ver', 'create_date', 'modified_date', 'trigger' ]) \
    .writeStream \
    .outputMode("append")\
    .option("multiline","true")\
    .format("console") \
    .start()

    # Wait for the stream processing to finish
    query.awaitTermination()

# entry point for PySpark ETL application
if __name__ == '__main__':
    main(kafkaBrokers, topic)
