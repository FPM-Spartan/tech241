# Create s3 bucket with python script

# 1. Import boto3 library
import boto3

# 2. set up a s3 connection
s3 = boto3.client('s3')

# 3. Create a bucket in the correct region (eu-west-1)
bucket_name = s3.create_bucket(Bucket="tech241-peter-python-bucket", CreateBucketConfiguration={"LocationConstraint":"eu-west-1"})

# 4. print bucket name to confirm the script worked correctly.
print(bucket_name)