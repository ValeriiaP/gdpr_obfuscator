import boto3
import botocore
import urllib.parse as urlparse

def read_file_s3(s3_path: str) -> None:
    """Reads a file from an S3 bucket.
        args: 
        file_name: str
        return: 
        data from the file in the S3 bucket
    """	
    try:
        parsed_url = urlparse.urlparse(s3_path)
        bucket_name = parsed_url.netloc
        file_key = parsed_url.path.lstrip('/')
        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        body = obj['Body']
        data = body.read().decode('utf-8')
        print('File read successfully')
        return data
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The file does not exist.")
        else:
            raise

read_file_s3('s3://test-bucket-270824/input/test.csv')

