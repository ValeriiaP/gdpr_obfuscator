import unittest
from unittest.mock import patch
import pandas as pd
from scr.mask_sensitive_data import mask_sensitive_data as mask_data


class TestMaskSensitiveData(unittest.TestCase):
    def test_obfuscation_of_pii_fields(self):
        data = {'Name': ['Alisa'], 'Email': [
            'alisa@example.com'], 'Phone': ['123456789']}
        df = pd.DataFrame(data)
        pii_fields = ['Name', 'Email']
        expected_result = {'Name': {0: '***'},
                           'Email': {0: '***'}, 'Phone': {0: '123456789'}}
        self.assertEqual(mask_data(df, pii_fields).to_dict(), expected_result)

    def test_obfuscation_if_some_pii_fields_missing(self):
        data = {'Name': ['Bob'], 'Email': ['bob@example.com']}
        df = pd.DataFrame(data)
        pii_fields = ['Name', 'Phone']
        expected_result = {'Name': {0: '***'}, 'Email': {0: 'bob@example.com'}}
        self.assertEqual(mask_data(df, pii_fields).to_dict(), expected_result)

    @patch('logging.info')
    @patch('logging.warning')
    def test_obfuscation_no_sensitive_fields_provided(self,
                                                      mock_warning, mock_info):
        data = {'Name': ['Olena'], 'Email': ['olena@example.com']}
        df = pd.DataFrame(data)
        pii_fields = []
        expected_result = mask_data(df, pii_fields)
        mock_info.assert_called_once_with('No sensitive fields provided.')
        mock_warning.assert_not_called()
        pd.testing.assert_frame_equal(expected_result, df)

    @patch('logging.info')
    @patch('logging.warning')
    def test_no_sensitive_fields_in_dataframe(self, mock_warning, mock_info):
        data = {'Name': ['Olena'], 'Email': ['olena@example.com']}
        df = pd.DataFrame(data)
        pii_fields = ['Phone', 'Address']
        expected_result = mask_data(df, pii_fields)
        self.assertEqual(mock_warning.call_count, 2)
        mock_info.assert_not_called()
        pd.testing.assert_frame_equal(expected_result, df)

