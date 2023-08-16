from pyspark.sql import SparkSession


from lib.Session import getSparkSession
from lib.utils import read_kafka
from lib.utils import cast_raw_data 
from lib.logger import Log4j 

kafkaBrokers = "BRO1:9092"
topic = "fe-request"

def main(kafkaBrokers, topic):
    
    # Get and initialize SparkSession
    spark = getSparkSession() 
    
    # Get and initialize Logger instance
    logger = Log4j(spark) 
    
    logger.info("Starting Integra Comsumer")
       
    # Read data from Event from Kafka as a streaming DataFrame
    df_raw = read_kafka(spark ,kafkaBrokers, topic,logger) 
    
    # Cast Raw data from  Kafka
    df_casted = cast_raw_data(df_raw , logger )
    
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
