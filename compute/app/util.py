from pyspark.sql import SparkSession

def getSparkSession(env , appName ):
    spark = SparkSession.\
        builder.\
        appName(appName).\
        master('local[*]').\
        getOrCreate()
    return spark