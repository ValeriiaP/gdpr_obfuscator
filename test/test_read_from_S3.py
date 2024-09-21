import unittest
from unittest.mock import patch, MagicMock
import botocore
from io import StringIO, BytesIO
from scr.file_reader import read_from_S3


class TestReadFromS3(unittest.TestCase):

    @patch('boto3.client')
    def test_read_from_S3_csv(self, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3
        mock_s3.get_object.return_value = {
            'Body': BytesIO(b'col1,col2\nval1,val2')
        }

        params = {
            'bucket_name': 'test-bucket',
            'file_key': 'test.csv',
            'file_format': 'csv'
        }

        result = read_from_S3(params)
        self.assertIsInstance(result, StringIO)
        self.assertEqual(result.getvalue(), 'col1,col2\nval1,val2')
        mock_s3.get_object.assert_called_once_with(
            Bucket='test-bucket', Key='test.csv')

    @patch('boto3.client')
    def test_read_from_S3_parquet(self, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3
        mock_s3.get_object.return_value = {
            'Body': BytesIO(b'parquet data')
        }

        params = {
            'bucket_name': 'test-bucket',
            'file_key': 'test.parquet',
            'file_format': 'parquet'
        }

        result = read_from_S3(params)
        self.assertIsInstance(result, BytesIO)
        self.assertEqual(result.getvalue(), b'parquet data')
        mock_s3.get_object.assert_called_once_with(
            Bucket='test-bucket', Key='test.parquet')

    @patch('boto3.client')
    def test_read_from_S3_file_not_found(self, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3
        mock_s3.get_object.side_effect = botocore.exceptions.ClientError(
            {'Error': {'Code': '404'}}, 'GetObject'
        )

        params = {
            'bucket_name': 'test-bucket',
            'file_key': 'nonexistent.csv',
            'file_format': 'csv'
        }

        with self.assertRaises(botocore.exceptions.ClientError):
            read_from_S3(params)
        mock_s3.get_object.assert_called_once_with(
            Bucket='test-bucket', Key='nonexistent.csv')

    @patch('boto3.client')
    def test_read_from_s3_file_not_exist(self, mock_boto_client):
        mock_s3 = MagicMock()
        mock_s3.get_object.side_effect = FileNotFoundError(
            "The file does not exist.")
        mock_boto_client.return_value = mock_s3

        params = {
            'bucket_name': 'test-bucket',
            'file_key': 'nonexistent.csv',
            'file_format': 'csv'
        }

        with self.assertRaises(FileNotFoundError) as context:
            read_from_S3(params)

        self.assertEqual(str(context.exception), "The file does not exist.")

    @patch('boto3.client')
    def test_other_client_error(self, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3
        mock_s3.get_object.side_effect = botocore.exceptions.ClientError(
            {'Error': {'Code': '500'}}, 'GetObject'
        )

        params = {
            'bucket_name': 'test-bucket',
            'file_key': 'some_file.csv',
            'file_format': 'csv'
        }

        with self.assertRaises(botocore.exceptions.ClientError):
            read_from_S3(params)
        mock_s3.get_object.assert_called_once_with(
            Bucket='test-bucket', Key='some_file.csv')


if __name__ == '__main__':
    unittest.main()
