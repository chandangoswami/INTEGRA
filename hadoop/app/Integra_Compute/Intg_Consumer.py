###############################################################################
#                      PROPERTY OF                                            #
#    Enigma Incorporated . Calcutta- West Bengal                              #
#    Project    : INTEGRA                                                     #
#    Copyrights : Closed source                                               #
#    Verion     : 2023.1.0.0                                                  #
#    Author     : Chandan Kumar Goswami                                       #
#    File       : Integra_consumer.py                                         #
#    About      : This file contains main function of Integra compute and En- #
#                  try point for Kafka subscriber.                            #
#                 1. Spark session creation and config. loading               #
#                 2. Kafka consumner listener initialization                  #
#                 3. Data serialization and de-Serialization                  #
#                 4. Pydantic data validation of incoming kafka messages      #
#                                                                             #
###############################################################################

from pyspark.sql import SparkSession 
from lib.logger import Log4j 

from integra.com.Session import getSparkSession
from integra.com.utils import read_kafka, cast_raw_data
from integra.com.FlowSchema import * 
from integra.com.workflow_Processor import process_inputNodes, process_functionNodes, process_outPutNodes

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
 
    # Process each streaming DataFrame
    def process_batch_message(df_raw , index ) :
    # Cast Raw data from  Kafka
        flow_metaData = cast_raw_data( df_raw , logger ) 
        
        if flow_metaData.count() > 0 :
            for wf in flow_metaData.collect() :
                try:
                    rdict = wf.asDict(True)
                    pydRec = FlowMetaC(**rdict)
                    logger.info("Kafka Message  valid and proceeding with Input Node Processing") 
                    process_inputNodes(pydRec , logger )
                    logger.info("Input Node Processing Complete")
                    process_functionNodes(pydRec , logger )
                    logger.info("Function Node Processing Complete")
                    process_outPutNodes(pydRec , logger )
                    logger.info("OutPutNode Node Processing Complete\n Waiting for Next Workflow")    
                except ValueError as er :
                    print('Format error and ignoring the message : \n', er)
        
    query = df_raw.writeStream \
        .foreachBatch(process_batch_message) \
        .option("checkpointLocation", "/tmp") \
        .start().awaitTermination()
    
    logger.info("Stoping Integra Comsumer{}", type(query) )

# entry point for PySpark ETL application
if __name__ == '__main__':
    main(kafkaBrokers, topic)
    