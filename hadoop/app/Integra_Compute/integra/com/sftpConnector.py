
from lib.logger import Log4j 

from integra.com.FlowSchema import FlowMetaC , InputMetC

def sftpConnector( inputRec:InputMetC, logger: Log4j ) :
    logger.info("Fetching DataFrame from sFTP file " + inputRec.filename )
