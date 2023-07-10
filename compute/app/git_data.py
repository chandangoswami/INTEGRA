from util import getSparkSession
from read import from_files 
from pyspark.sql.functions import year, month, dayofmonth

env = "DEV" 
appName = "Datatest"
SRC_DIR = "./data/"
SRC_FORMAT = "json"
SRC_PATTERN = "2011-03-25-*.json"


spark = getSparkSession(env , appName )

git_data_df = from_files(spark,SRC_DIR,SRC_PATTERN,SRC_FORMAT) 

git_data_df.select("created_at").show()
git_data_df.withColumn("YEAR",year('created_at') ).select("repo*","YEAR").show()
