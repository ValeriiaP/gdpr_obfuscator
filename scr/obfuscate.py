from scr.data_parser import s3_path_parser as parser
from scr.file_reader import read_from_file
from scr.mask_sensitive_data import mask_sensitive_data, generate_masked_output
import json as JSON


def obfuscate(input: JSON) -> bytes:
    """ This function obfuscates sensitive data in the file.

    Args:
        file_to_obfuscate: str
        pii_fields: list of strings

    Returns:
    byte stream with masked data.
    """
    params = parser(input['file_to_obfuscate'])
    dataFrame = read_from_file(params)
    masked_df = mask_sensitive_data(dataFrame, input['pii_fields'])
    result = generate_masked_output(masked_df, params['file_format'])

    return result
