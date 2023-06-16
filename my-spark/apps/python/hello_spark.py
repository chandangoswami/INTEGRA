
import sys
from random import random
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession.builder.appName("Hello_spark").getOrCreate() 
    
    df = spark.read.option("header",True).csv("../../spark-data/emp_lst.csv")
    df.show()

    spark.stop()
