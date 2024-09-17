import unittest
from scr.obfuscate import obfuscate
from unittest.mock import patch, MagicMock
import json as JSON

class TestObfuscate(unittest.TestCase):

    @patch('scr.obfuscate.generate_masked_output')
    @patch('scr.obfuscate.mask_sensitive_data')
    @patch('scr.obfuscate.read_from_file')
    @patch('scr.obfuscate.parser')
    def test_obfuscate(self, mock_parser, mock_read_from_file, mock_mask_sensitive_data, mock_generate_masked_output):
        
        input_data = {
            'file_to_obfuscate': 's3://my_bucket/new_data/file.csv',
            'pii_fields': ['name', 'email']
        }
        mock_params = {'file_format': 'csv'}
        mock_df = MagicMock()
        mock_masked_df = MagicMock()
        mock_result = b'masked data'

        mock_parser.return_value = mock_params
        mock_read_from_file.return_value = mock_df
        mock_mask_sensitive_data.return_value = mock_masked_df
        mock_generate_masked_output.return_value = mock_result

        result = obfuscate(input_data)

        mock_parser.assert_called_once_with(input_data['file_to_obfuscate'])
        mock_read_from_file.assert_called_once_with(mock_params)
        mock_mask_sensitive_data.assert_called_once_with(mock_df, input_data['pii_fields'])
        mock_generate_masked_output.assert_called_once_with(mock_masked_df, mock_params['file_format'])
        self.assertEqual(result, mock_result)

if __name__ == '__main__':
    unittest.main()