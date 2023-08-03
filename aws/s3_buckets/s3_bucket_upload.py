# Upload to s3 bucket with python

# 1. Import boto3

import boto3

# 2. Set up a s3 connection
s3 = boto3.client('s3')

# 3. Upload specified file to the specified bucket and give it a specified filename.

file_upload = s3.upload_file("testfile.txt", "tech241-peter-python-bucket", "testfileupload.txt")

