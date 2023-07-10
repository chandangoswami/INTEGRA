from util import getSparkSession

env = "DEV" 
appName = "Datatest"

spark = getSparkSession(env , appName )

spark.sql("select current_date ").show()
