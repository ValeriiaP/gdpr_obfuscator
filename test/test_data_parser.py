import unittest
from scr.data_parser import s3_path_parser


class TestS3PathParser(unittest.TestCase):
    def test_valid_s3_path(self):

        s3_path = "s3://bucket-name/folder/file.txt"
        expected_result = ({"bucket_name": 'bucket-name',
                            "file_key": 'folder/file.txt',
                            "file_format": 'txt'})
        self.assertEqual(s3_path_parser(s3_path), expected_result)

    def test_path_with_special_chars(self):

        s3_path = "s3://bucket-name/folder/!@$%^&*()_+=-{}[].txt"
        expected_result = ({"bucket_name": 'bucket-name',
                            "file_key": 'folder/!@$%^&*()_+=-{}[].txt',
                            "file_format": 'txt'})
        self.assertEqual(s3_path_parser(s3_path), expected_result)

    def test_path_with_no_folder(self):

        s3_path = "s3://bucket-name/file.txt"
        expected_result = ({"bucket_name": 'bucket-name',
                            "file_key": 'file.txt', "file_format": 'txt'})
        self.assertEqual(s3_path_parser(s3_path), expected_result)


if __name__ == '__main__':
    unittest.main()
