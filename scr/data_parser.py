import urllib.parse as urlparse


def s3_path_parser(s3_path: str) -> dict:
    """This function parse the s3 path into:
    - bucket_name,
    - file_key
    - file format.

    Args:
        str: s3 path

    Returns:
        dict: dictionary with next keys: bucket_name, file_key and file format.

    """
    try:
        if not s3_path.startswith("s3://"):
            raise ValueError("Invalid S3 path, it should start with 's3://'")
        parsed_url = urlparse.urlparse(s3_path)
        bucket_name = parsed_url.netloc
        file_key = parsed_url.path.lstrip('/')
        file_format = file_key.split('.')[-1]

        return {"bucket_name": bucket_name,
                "file_key": file_key,
                "file_format": file_format}
    except Exception as e:
        raise ValueError(f"Invalid S3 path: {s3_path}. Error: {str(e)}")
