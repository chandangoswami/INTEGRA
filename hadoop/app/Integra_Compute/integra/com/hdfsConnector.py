
from lib.logger import Log4j 

from integra.com.FlowSchema import FlowMetaC , InputMetC

def hdfsConnector( inputRec:InputMetC, logger: Log4j ) :
    logger.info("Fetching DataFrame from HDFS file " + inputRec.filename )
