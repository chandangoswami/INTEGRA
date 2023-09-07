from pyspark.sql import SparkSession 

from lib.logger import Log4j 
from integra.com.Session import getSparkSession
from integra.com.utils import read_kafka, cast_raw_data 
from integra.parser  import parseInput 

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
    
    
    def process_batch_message(df_raw, batch_id ) :
           # Cast Raw data from  Kafka
            flow_metaData = cast_raw_data(df_raw , logger )
            print(type(flow_metaData))
            
            if flow_metaData.count() > 0 :
               for wf in flow_metaData.collect() :
                flow_metaData.show()

    query = df_raw.writeStream \
        .foreachBatch(process_batch_message) \
        .option("checkpointLocation", "/tmp") \
        .start().awaitTermination()
    
    logger.info("Stoping Integra Comsumer{}", type(query) )

# entry point for PySpark ETL application
if __name__ == '__main__':
    main(kafkaBrokers, topic)
