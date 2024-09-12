import pandas as pd
import io
import logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.warning)


def mask_sensitive_data(
        dataframe: pd.DataFrame, pii_fields: list) -> pd.DataFrame:
    """ This function mask sensitive data in the dataframe.

    Args:
        DataFrame: DataFrame from file
        list (str): pii_fields

    Returns:
        DataFrame: DataFrame with replaced sensitive information
    """

    for field in pii_fields:
        if field in dataframe.columns:
            dataframe[field] = '***'
        else:
            logging.warning(f"Field '{field}' not found in dataframe columns.")
    return dataframe


def generate_masked_output(
        masked_df: pd.DataFrame, file_format) -> bytes:
    """ This function creates byte-stream from dataframe.

    Args:
        DataFrame: masked DataFrame

    Returns:
        bytes: file in json, csv format or byte-stream with masked data.
    """
    try:
        if file_format == 'csv':
            byte_stream = io.BytesIO()
            masked_df.to_csv(byte_stream, index=False)
            byte_stream_value = byte_stream.getvalue()
            logging.info('Byte stream value is written')
            return byte_stream_value
        if file_format == 'json':
            byte_stream = io.BytesIO()
            masked_df.to_json(byte_stream, orient='records', lines=True)
            byte_stream_value = byte_stream.getvalue()
            logging.info('Byte stream value is written')
            return byte_stream_value
        if file_format == 'parquet':
            byte_stream = io.BytesIO()
            masked_df.to_parquet(byte_stream, index=False)
            byte_stream_value = byte_stream.getvalue()
            logging.info('Byte stream value is written')
            return byte_stream_value
        else:
            logging.error(
                f"Invalid file format: {file_format}")
    except Exception as e:
        logging.error(f"Error creating byte-stream: {e}")
        raise
