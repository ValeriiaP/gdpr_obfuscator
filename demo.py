import boto3
from scr.obfuscate import obfuscate
import time

s3 = boto3.client('s3')


"""Test json format"""
start_time = time.time()
test_data_json = obfuscate({
    "file_to_obfuscate": 's3://test-bucket-030924/input/students.json',
    "pii_fields": ["name", "email_address"]
})
end_time = time.time()
runtime = end_time - start_time
print(f"Runtime: {runtime} seconds")
object_json = s3.put_object(Bucket='test-bucket-030924',
                            Key='output/output.json',
                            Body=test_data_json)


"""Test csv format"""
start_time = time.time()
test_data_csv = obfuscate({
    "file_to_obfuscate":
    's3://test-bucket-030924/test_students.csv',
    "pii_fields": ["name", "email_address"]
})
end_time = time.time()
runtime = end_time - start_time
print(f"Runtime: {runtime} seconds")
object_csv = s3.put_object(Bucket='test-bucket-030924',
                           Key='output/output.csv',
                           Body=test_data_csv)


"""Test parquet format"""
start_time = time.time()
test_data_parquet = obfuscate({
    "file_to_obfuscate":
    's3://test-bucket-030924/parquet/test_students.parquet',
    "pii_fields": ["name", "email_address"]
})
end_time = time.time()
runtime = end_time - start_time
print(f"Runtime: {runtime} seconds")
object_parquet = s3.put_object(Bucket='test-bucket-030924',
                               Key='output/output.parquet',
                               Body=test_data_parquet)


# with open('output.json', 'wb') as f:
#     f.write(test_data_json)
# with open('output.csv', 'wb') as f:
#     f.write(test_data_csv)
# with open('output.parquet', 'wb') as f:
#     f.write(test_data_parquet)
