import configparser

from pyspark import SparkConf
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import col,from_json 
from pyspark.sql.dataframe import DataFrame 
from lib.logger import Log4j

from integra.com.FlowSchema import *

def load_survey_df(spark, data_file):
    return spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(data_file)


def count_by_country(survey_df):
    return survey_df.filter("Age < 40") \
        .select("Age", "Gender", "Country", "state") \
        .groupBy("Country") \
        .count()


def get_spark_app_config():
    spark_conf = SparkConf()
    config = configparser.ConfigParser()
    config.read("spark.conf")

    for (key, val) in config.items("SPARK_APP_CONFIGS"):
        spark_conf.set(key, val)
    return spark_conf

def read_kafka (spark ,kafkaBrokers, topic, logger ) : 
    
    logger.info(f"Listining kafka Queue Topic Name [ {topic} ] and Servers [ {kafkaBrokers} ] ")
    
    return spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafkaBrokers) \
    .option("subscribe", topic) \
    .option("startingOffsets", "earliest") \
    .load() 
    
def cast_raw_data ( df_raw:DataFrame , logger: Log4j ) :
   
    df_casted = (df_raw
    .withColumn("key", df_raw["key"].cast(StringType()))
    .withColumn("value", df_raw["value"].cast(StringType()))
    ).select('value').withColumn("jsonData",from_json(col("value"),flowMetaSchema)).select("jsonData.*")    
   
    return df_casted
