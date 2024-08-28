import pandas as pd
import io
import logging
import read_file_s3 as rf

logging.basicConfig(level=logging.INFO)


def mask_sensitive_data(dataframe: pd.DataFrame, pii_fields: list) -> pd.DataFrame:
    """ This function mask sensitive data in the dataframe.

    Args:
        dataframe: DataFrame
        pii_fields: list of strings

    Returns:
    DataFrame with replacing sensitive information.

    """
    for field in pii_fields:
        if field in dataframe.columns:
            dataframe[field] = '***'
        else:
            logging.warning(f"Field '{field}' not found in dataframe columns.")
    return dataframe


def create_masked_csv_or_byte_stream(masked_df: pd.DataFrame, type_result: str) -> None:
    """ This function creates a masked csv file.

    Args:
        dataframe: DataFrame
        type_result: str

    Returns:
    csv file with masked data or byte stream.
    """
    try:
        if type_result == 'csv':
            return masked_df.to_csv('result.csv', index=False, encoding='utf-8')
        else:
            byte_stream = io.BytesIO()
            masked_df.to_csv(byte_stream, index=False)
            byte_stream_value = byte_stream.getvalue()
            logging.info(byte_stream_value)
            print(byte_stream_value)
    except Exception as e:
        logging.error(f"Error CSV file: {e}")
