

import __main__
from os import environ, listdir, path

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import col,from_json


def getSparkSession():
        
    spark = SparkSession.builder \
    .appName("IntegraConsumer") \
    .master("local[*]") \
    .getOrCreate()
    
    return spark