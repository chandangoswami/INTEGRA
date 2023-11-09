
import io
import pandas as pd
import paramiko
from lib.logger import Log4j 

from integra.com.FlowSchema import FlowMetaC , InputMetC

def sftp2pddf(hostname , userid , passwd , port, dirname, filename ) : 
   abspath =dirname+'/'+filename

   transport = paramiko.Transport((hostname , port ))
   transport.connect(username=userid , password=passwd )
   sftp = transport.open_sftp_client()
   with sftp.open(abspath , 'r') as remote_file:
     file_contents = remote_file.read()

   sftp.close()
   transport.close() 

   string_data = file_contents.decode('utf-8')
   pddf = pd.read_csv(io.StringIO(string_data))

   return pddf 

def pddf2sftp(hostname , userid , passwd , port, dirname, filename, df ) : 
   abspath =dirname+'/'+filename

   transport = paramiko.Transport((hostname , port ))
   transport.connect(username=userid , password=passwd )
   sftp = transport.open_sftp_client()

   with sftp.open(abspath , 'w+') as remote_file:
     file_contents = remote_file.read()

   sftp.close()
   transport.close() 

   string_data = file_contents.decode('utf-8')
   pddf = pd.read_csv(io.StringIO(string_data))

   return pddf 


def sftpConnector( inputRec:InputMetC, logger: Log4j ) -> pd :
    
    hostname = inputRec.connectString.endPoint
    userid = inputRec.connectString.userID
    passwd = inputRec.connectString.passwd
    port= inputRec.connectString.port
    dirname = inputRec.folder 
    filename = inputRec.filename
    
    logger.debug(f"Hostname {hostname} userid {userid} passwd {passwd} port {port} dirname {dirname} filename {filename} " )
        
    try:
       df = sftp2pddf ( hostname, userid, passwd, port , dirname , filename )
      # print(df.head())
       return df 
    
    except Exception as e :
      logger.error(f" sftp error occurred : {str(e)} while reading from {hostname} fileName {filename} user folder {dirname} ")
      raise Exception("sFtp input Error!") 