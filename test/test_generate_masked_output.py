import unittest
import pandas as pd
from unittest import mock
from scr.mask_sensitive_data import generate_masked_output


class TestGenerateMaskedOutput(unittest.TestCase):

    def setUp(self):
        """Set up a sample dataframe for testing."""
        self.sample_data_frame = pd.DataFrame([
            {
                "Name": "John Doe",
                "Email": "johndoe@example.com",
                "Phone": "123-456-7890",
                "Address": "123 Elm St",
            },
            {
                "Name": "Jane Smith",
                "Email": "janesmith@example.com",
                "Phone": "234-567-8901",
                "Address": "456 Oak St",
            }
        ])

    @mock.patch('pandas.DataFrame.to_csv')
    @mock.patch('io.BytesIO')
    @mock.patch('logging.info')
    def test_generate_csv_byte_stream(self, mock_logging_info,
                                      mock_bytes_io, mock_to_csv):
        """Test the generation of a CSV byte-stream."""
        result = generate_masked_output(
            self.sample_data_frame, 'csv')
        mock_to_csv.assert_called_once_with(mock_bytes_io(), index=False)
        self.assertIsNotNone(result)
        mock_logging_info.assert_called_once_with(
            'Byte stream value is written')

    @mock.patch('pandas.DataFrame.to_json')
    @mock.patch('io.BytesIO')
    @mock.patch('logging.info')
    def test_generate_json_byte_stream(self, mock_logging_info,
                                       mock_bytes_io, mock_to_json):
        """Test the generation of a JSON byte-stream."""
        result = generate_masked_output(
            self.sample_data_frame, 'json')
        mock_to_json.assert_called_once_with(
            mock_bytes_io(), orient='records', lines=True)
        self.assertIsNotNone(result)
        mock_logging_info.assert_called_once_with(
            'Byte stream value is written')

    @mock.patch('pandas.DataFrame.to_parquet')
    @mock.patch('io.BytesIO')
    @mock.patch('logging.info')
    def test_generate_parquet_byte_stream(self, mock_logging_info,
                                          mock_bytes_io, mock_to_parquet):
        """Test the generation of a Parquet byte-stream."""
        result = generate_masked_output(
            self.sample_data_frame, 'parquet')
        mock_to_parquet.assert_called_once_with(mock_bytes_io(), index=False)
        self.assertIsNotNone(result)
        mock_logging_info.assert_called_once_with(
            'Byte stream value is written')

    @mock.patch('logging.error')
    def test_error_handling(self, mock_logging_error):
        """Test exception handling during file generation."""
        with mock.patch('pandas.DataFrame.to_json',
                        side_effect=Exception('Test Error')):
            with self.assertRaises(Exception) as context:
                generate_masked_output(self.sample_data_frame, 'json')
            mock_logging_error.assert_called_once_with(
                'Error creating byte-stream: Test Error')
            self.assertEqual(str(context.exception), 'Test Error')

    @mock.patch('logging.error')
    def test_invalid_file_format(self, mock_logging_error):
        """Test invalid file format."""
        generate_masked_output(self.sample_data_frame, 'invalid')
        mock_logging_error.assert_called_once_with(
            'Invalid file format: invalid')


if __name__ == '__main__':
    unittest.main()
