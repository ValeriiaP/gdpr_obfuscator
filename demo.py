import boto3
from scr.obfuscate import obfuscate

test_data_json = obfuscate({
    "file_to_obfuscate": 's3://test-bucket-030924/input/students.json',
    "pii_fields": ["name", "email_address"]
})

test_data_csv = obfuscate({
    "file_to_obfuscate": 's3://test-bucket-030924/test.csv',
    "pii_fields": ["Name", "Email"]
})

with open('output.json', 'wb') as f:
    f.write(test_data_json)

s3 = boto3.client('s3')
object = s3.put_object(Bucket='test-bucket-030924',
                       Key='output/output.json', Body=test_data_json)
# object = s3.put_object(Bucket='test-bucket-030924',
                    #    Key='output/output.csv', Body=test_data_csv)
