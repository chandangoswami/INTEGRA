import pandas as pd
import numpy as np
import paramiko
import io

hostname='hadoop-sftp-1'
userid='user1'
passwd='bpt799'
port=22
dirname ='/home/user1' 
filename ='sample.csv'

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

try:
   df = sftp2pddf ( hostname, userid, passwd, port , dirname , filename )
   print(df.head())

except Exception as e :
   print(f"An error occurred: {str(e)}")

