import boto3

s3 = boto3.client('s3')

s3.list_buckets()