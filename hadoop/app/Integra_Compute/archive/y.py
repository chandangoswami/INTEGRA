import pandas as pd
import pysftp

hostname='hadoop-sftp-1'
port='22'
username='user1'
password='bpt799'
path='/home/user1/sample.csv'

cnopts = pysftp.CnOpts()
with pysftp.Connection(
        host=hostname,
        port=port,
        username=username,
        password=password,
        cnopts=cnopts,
    ) as sftp:
        with sftp.open(path, 'rb') as dst_file:
            
            df = pd.read_csv( dst_file)
            print(df)
