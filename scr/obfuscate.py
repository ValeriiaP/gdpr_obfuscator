from data_parser import s3_path_parser as parser
from file_reader import read_from_file
from mask_sensitive_data import mask_sensitive_data
from mask_sensitive_data import generate_masked_output
import json as JSON


def obfuscate(input: JSON, type_result: str) -> None:
    """ This function obfuscates sensitive data in the file.

    Args:
        file_to_obfuscate: str
        pii_fields: list of strings

    Returns:
    csv, json file or byte stream with masked data.

    """
    params = parser(input['file_to_obfuscate'])
    dataFrame = read_from_file(params)
    masked_df = mask_sensitive_data(dataFrame, input['pii_fields'])
    result = generate_masked_output(masked_df,
                                    type_result, params['file_format'])

    return result


obfuscate({
    "file_to_obfuscate": 's3://test-bucket-030924/input/test.json',
    "pii_fields": ["Name", "Email"]
}, 'byte-stream')
