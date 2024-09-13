import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from io import StringIO, BytesIO
from scr.file_reader import read_from_file

class TestReadFromFile(unittest.TestCase):

    @patch('scr.file_reader.read_from_S3')
    def test_read_from_file_csv(self, mock_read_from_S3):
        mock_read_from_S3.return_value = StringIO('col1,col2\nval1,val2')

        params = {
            'bucket_name': 'test-bucket',
            'file_key': 'test.csv',
            'file_format': 'csv'
        }

        result = read_from_file(params)
        expected_df = pd.DataFrame({'col1': ['val1'], 'col2': ['val2']})
        pd.testing.assert_frame_equal(result, expected_df)
        mock_read_from_S3.assert_called_once_with(params)

    @patch('scr.file_reader.read_from_S3')
    def test_read_from_file_json(self, mock_read_from_S3):
        mock_read_from_S3.return_value = StringIO('{"col1": ["val1"], "col2": ["val2"]}')

        params = {
            'bucket_name': 'test-bucket',
            'file_key': 'test.json',
            'file_format': 'json'
        }

        result = read_from_file(params)
        expected_df = pd.DataFrame({'col1': ['val1'], 'col2': ['val2']})
        pd.testing.assert_frame_equal(result, expected_df)
        mock_read_from_S3.assert_called_once_with(params)

    @patch('scr.file_reader.read_from_S3')
    def test_read_from_file_parquet(self, mock_read_from_S3):
        mock_read_from_S3.return_value = BytesIO(b'parquet data')
        with patch('pandas.read_parquet') as mock_read_parquet:
            mock_read_parquet.return_value = pd.DataFrame({'col1': ['val1'], 'col2': ['val2']})

            params = {
                'bucket_name': 'test-bucket',
                'file_key': 'test.parquet',
                'file_format': 'parquet'
            }

            result = read_from_file(params)
            expected_df = pd.DataFrame({'col1': ['val1'], 'col2': ['val2']})
            pd.testing.assert_frame_equal(result, expected_df)
            mock_read_from_S3.assert_called_once_with(params)
            mock_read_parquet.assert_called_once()

    @patch('scr.file_reader.read_from_S3')
    def test_read_from_file_unsupported_format(self, mock_read_from_S3):
        params = {
            'bucket_name': 'test-bucket',
            'file_key': 'test.txt',
            'file_format': 'txt'
        }

        with self.assertRaises(ValueError):
            read_from_file(params)
        mock_read_from_S3.assert_called_once_with(params)

    @patch('scr.file_reader.read_from_S3')
    def test_read_from_file_exception(self, mock_read_from_S3):
        mock_read_from_S3.side_effect = Exception("Some error")

        params = {
            'bucket_name': 'test-bucket',
            'file_key': 'test.csv',
            'file_format': 'csv'
        }

        with self.assertRaises(Exception):
            read_from_file(params)
        mock_read_from_S3.assert_called_once_with(params)


if __name__ == '__main__':
    unittest.main()