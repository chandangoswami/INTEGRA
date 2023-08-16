import configparser

from pyspark import SparkConf
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import col,from_json 

def get_spark_app_config():
    spark_conf = SparkConf()
    config = configparser.ConfigParser()
    config.read("spark.conf")

    for (key, val) in config.items("SPARK_APP_CONFIGS"):
        spark_conf.set(key, val)
    return spark_conf

def read_kafka (spark ,kafkaBrokers, topic, logger ) : 
    return spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafkaBrokers) \
    .option("subscribe", topic) \
    .load()
    
def cast_raw_data ( df_raw , logger) :
    
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
         
    return df_casted