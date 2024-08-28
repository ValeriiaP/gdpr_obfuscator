import urllib.parse as urlparse


def s3_path_parser(s3_path: str) -> None:
    """This function parse the s3 path into:
    - bucket_name,
    - file_key
    - file format.

    Args:
        s3_path: str

    Returns:
    dictionary with next keys: bucket_name, file_key and file format.

    """
    parsed_url = urlparse.urlparse(s3_path)
    bucket_name = parsed_url.netloc
    file_key = parsed_url.path.lstrip('/')
    file_format = file_key.split('.')[-1]

    return {"bucket_name": bucket_name,
            "file_key": file_key,
            "file_format": file_format}
