from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import col,from_json

# Create a SparkSession
spark = SparkSession.builder.appName("JSONStreaming").getOrCreate()

df_js = spark.read.text("./flowMetaFormat.txt")

df_js.printSchema()
df_js.show()

flow_schema =  StructType ([
StructField("wfName",StringType(),True),
StructField("wfType",StringType(),True),
StructField("wfId",StringType(),True),
StructField("ver",StringType(),True),
StructField("create_date",StringType(),True),
StructField("modified_date",StringType(),True),
StructField("trigger",StringType(),True) 
])

dfJSON = df_js.withColumn("jsonData",from_json(col("value"),flow_schema)).select("jsonData.*")

dfJSON.printSchema()
dfJSON.show(truncate=False)