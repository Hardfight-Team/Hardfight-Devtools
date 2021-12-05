# External imports
from typing import Any
import botocore  # type: ignore
import sys


# AWS informations (for upload)
AWS_BUCKET = 'download.hardfight.fr'


def upload_file(s3_client: Any, file_path: str, obj_name: str,
                bucket: str = AWS_BUCKET):
    """Upload public file to the AWS hardfight download bucket
    :note: Exits(1) if the upload fail

    :param s3_client:   S3 client instance
    :type s3_client:    Any
    :param file_path:   File to upload
    :type file_path:    str
    :param obj_name:    Object name in the bucket
    :param obj_name:    str
    :param bucket:      Bucket to upload to, defaults to AWS_BUCKET
    :param bucket:      str
    """
    try:
        s3_client.upload_file(file_path, bucket, obj_name,
                              ExtraArgs={'ACL': 'public-read'})
    except botocore.exceptions.ClientError as err:
        print(err, file=sys.stderr)
        sys.exit(1)
