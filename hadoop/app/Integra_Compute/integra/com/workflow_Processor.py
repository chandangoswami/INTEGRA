from lib.logger import Log4j 

from integra.com.FlowSchema import FlowMetaC , InputMetC
from integra.com.sftpConnector import * 
from integra.com.hdfsConnector import *  

        
def process_inputNodes(wf_meta:FlowMetaC , logger:Log4j ) :
    logger.info("Input node processing \n Creating DataFrame Lists") 
    input_collection = wf_meta.inputNode 
    
    for dsrc in input_collection:
        match dsrc.nodeType : 
            case "IN_SFTP" :
                sftpConnector(dsrc, logger) 
            case "HDFS":
                dFTP = hdfsConnector(dsrc, logger)
            case _:
                logger.error("Unidentified inPut Node Type " + dsrc.nodeType + "\n Type FATAL ERROR!!" )  
                # TBD THOW ERROR and STOP 
             

def process_functionNodes(wf_meta:FlowMetaC , logger:Log4j ) :
    logger.info("Function node processing \n Creating DataFrame Lists for function Nodes") 

def process_outPutNodes(wf_meta:FlowMetaC , logger:Log4j ) :
    logger.info("Function node processing \n Creating DataFrame Lists for function Nodes")
    