import boto3
from scr.obfuscate import obfuscate

s3 = boto3.client('s3')


"""Test json format"""
test_data_json = obfuscate({
    "file_to_obfuscate": 's3://test-bucket-030924/input/students.json',
    "pii_fields": ["name", "email_address"]
})
object_json = s3.put_object(Bucket='test-bucket-030924',
                            Key='output/output.json',
                            Body=test_data_json)


"""Test csv format"""
test_data_csv = obfuscate({
    "file_to_obfuscate": 's3://test-bucket-030924/test.csv',
    "pii_fields": ["Name", "Email"]
})
object_csv = s3.put_object(Bucket='test-bucket-030924',
                           Key='output/output.csv',
                           Body=test_data_csv)


"""Test parquet format"""
test_data_parquet = obfuscate({
    "file_to_obfuscate": 's3://test-bucket-030924/parquet/test.parquet',
    "pii_fields": ["name", "email_address"]
})
object_parquet = s3.put_object(Bucket='test-bucket-030924',
                               Key='output/output.parquet',
                               Body=test_data_parquet)


# with open('output.json', 'wb') as f:
#     f.write(test_data_json)
# with open('output.csv', 'wb') as f:
#     f.write(test_data_csv)
# with open('output.parquet', 'wb') as f:
#     f.write(test_data_parquet)
