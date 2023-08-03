# delete a s3 bucket using python

# 1. import boto3

import boto3

# 2. set connection to s3

s3 = boto3.resource("s3")

# 3. delete bucket

bucket = s3.Bucket("tech241-peter-python-bucket")
response = bucket.delete()

# 4. print response to confirm script has worked correctly.
print(response)