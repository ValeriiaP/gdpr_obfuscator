import boto3
import botocore
from io import StringIO
import pandas as pd


def read_from_S3(params: dict) -> StringIO:
    """This function reads the file from an S3 bucket.
    args:
        params: dict
    return:
        data from the file from S3
    """

    try:
        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket=params['bucket_name'],
                            Key=params['file_key'])
        body = obj['Body'].read().decode('utf-8')
        data = StringIO(body)
        return data
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The file does not exist.")
        else:
            raise


def read_from_file(params: dict) -> pd.DataFrame:
    """This function reads a data from a file in S3 bucket.
    args:
        params: dict
    return:
        dataframe with the data from the file.
    """
    try:
        data = read_from_S3(params)

        if params['file_format'] == 'csv':
            df = pd.read_csv(data)
            return df
        if params['file_format'] == 'json':
            df = pd.read_json(data)
            return df
        else:
            raise ValueError("The file format is not supported")
    except Exception:
        print("Error reading the file")
        raise
