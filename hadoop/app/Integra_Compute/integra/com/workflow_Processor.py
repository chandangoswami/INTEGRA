from lib.logger import Log4j 

from integra.com.FlowSchema import FlowMetaC , InputMetC
from integra.com.sftpConnector import * 
from integra.com.hdfsConnector import *  

        
def process_inputNodes(wf_meta:FlowMetaC , logger:Log4j ) -> list :
     
    logger.info("==> STEP-2 Input Nodes Processing <== ")
    inData = [] 
    
    try:
        input_collection = wf_meta.inputNode 
        for dsrc in input_collection:
            match dsrc.nodeType : 
                case "IN_SFTP" :
                  inData.append(sftpConnector(dsrc, logger))  
                case "HDFS":
                    dFTP = hdfsConnector(dsrc, logger)
                case _:
                    logger.error("Unidentified inPut Node Type " + dsrc.nodeType + "\n Type FATAL ERROR!!" )  
                    # TBD THOW ERROR and STOP
        return inData 
    except Exception as e :
       logger.error(f"An error occurred: {str(e)}")
         
def process_functionNodes(wf_meta:FlowMetaC , inDfList:list , logger:Log4j ) :
    logger.info("==> STEP-3 Function Nodes Processing <== ")
    [print(df) for df in inDfList ]
    

def process_outPutNodes(wf_meta:FlowMetaC , logger:Log4j ) : 
    logger.info("==> STEP-4 OutPut Nodes Processing <== ")
    