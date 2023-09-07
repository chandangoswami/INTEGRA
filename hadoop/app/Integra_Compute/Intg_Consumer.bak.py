from pyspark.sql import SparkSession
#from lib.Session import getSparkSession
from lib.utils import read_kafka
from lib.utils import cast_raw_data 
from lib.logger import Log4j 
from integra.com.Session2 import getSparkSession


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
    flow_metaData = cast_raw_data(df_raw , logger )

    #df_input_meta = df_casted.select(['input'])
    #df_funtion_meta = df_casted.select(['function'])
    #df_output_meta = df_casted.select(['output'])

#    workFl_meta = flow_metadata.select(['wfName', 'wfType', 'wfId', 'ver', 'create_date', 'modified_date', 'trigger' ]) 
#    input_meta = flow_metadata.select(['wfName', 'wfType', 'wfId', 'ver', 'create_date', 'modified_date', 'trigger' ]) 
#    output_meta = flow_metadata.select(['wfName', 'wfType', 'wfId', 'ver', 'create_date', 'modified_date', 'trigger' ]) 

#    Desired state code
#    input_meta, process_meta, output_meta = parse_WF_metaData( flow_metaData )
#    df_input[] = process_input(input_meta ) 
#    df_funct[] = process_function(df_input[] ) 
#    eltRepot[] = process_output (df_funct[] ) 


    query = flow_metaData.select(['wfName', 'wfType', 'wfId', 'ver', 'create_date', 'modified_date', 'trigger' ]) \
    .writeStream \
    .outputMode("append")\
    .option("multiline","true")\
    .format("console") \
    .start()

    # Wait for the stream processing to finish
    query.awaitTermination()

    logger.info("Stoping Integra Comsumer")

# entry point for PySpark ETL application
if __name__ == '__main__':
    main(kafkaBrokers, topic)