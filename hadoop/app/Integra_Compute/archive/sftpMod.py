import paramiko

# SFTP connection parameters
hostname = 'localost'  # Replace with your SFTP server hostname
port = 2023                      # Default SFTP port is 22
username = 'user1'      # Replace with your SFTP username
password = 'bpt799'      # Replace with your SFTP password (or use SSH key)

# Remote file path on the SFTP server
remote_file_path = '/home/user1/av1.txt'

# Local file path where you want to save the downloaded file
local_file_path = './av1.txt'

try:
    # Create an SFTP client session
    transport = paramiko.Transport((hostname, port))
    transport.connect(username=username, password=password)

    # Create an SFTP client object
    sftp = transport.open_sftp()

    # Download the file from the SFTP server to the local machine
    sftp.get(remote_file_path, local_file_path)

    # Close the SFTP session
    sftp.close()

    # Close the transport session
    transport.close()

    print(f"File '{remote_file_path}' downloaded successfully to '{local_file_path}'")

except Exception as e:
    print(f"An error occurred: {str(e)}")

