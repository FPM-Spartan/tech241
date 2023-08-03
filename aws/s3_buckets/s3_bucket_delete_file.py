# delete an item in an s3 bucket with python

# 1. import boto3

import boto3

# 2. set up s3 connection

s3 = boto3.client('s3')

# 3. Delete item in bucket

item_delete = s3.delete_object(Bucket="tech241-peter-python-bucket", Key="testfileupload.txt")
