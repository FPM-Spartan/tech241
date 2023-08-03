# read/download a file from a s3 bucket using python

# 1. import boto3
import boto3

# 2. set up connection to s3

s3 = boto3.client('s3')

# 3. Download specified files from specified bucket

download_file = s3.download_file("tech241-peter-python-bucket", "testfileupload.txt", "testfiledownload.txt")

print(s3.download_file)