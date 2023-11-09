import paramiko
import pandas as pd
from io import StringIO

# SFTP server connection parameters
sftp_host = 'hadoop-sftp-1'
sftp_port = 22  # Default SFTP port is 22
sftp_username = 'user1'
sftp_password = 'bpt799'
sftp_remote_path = '/home/user1'  # Path to the remote directory containing the file

# File to read from the SFTP server
remote_filename = 'sample.csv'

# Establish an SFTP connection

transport = paramiko.Transport((sftp_host, sftp_port))

transport.connect(username=sftp_username, password=sftp_password)

sftp = transport.open_sftp_client()
# Construct the remote file path
remote_filepath = f'{sftp_remote_path}/{remote_filename}'

# Read the file contents from the SFTP server
with sftp.open(remote_filepath, 'r') as remote_file:
    file_contents = remote_file.read()

# Close the SFTP connection
sftp.close()
transport.close()

data = StringIO(str(file_contents))
print(type(file_contents))
print(type(data))

print((str(file_contents)) )

# Create a DataFrame from the file contents
df = pd.read_csv(data)
#df = pd.read_csv(StringIO(file_contents))

# Now, you have your DataFrame (df) with the data from the remote file
#print(df.head())
