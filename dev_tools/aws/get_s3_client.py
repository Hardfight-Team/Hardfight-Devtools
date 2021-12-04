# External imports
from typing import Any, Tuple, cast
import boto3    # type: ignore
import sys
import os


# Env variables names holding AWS credentials
AWS_KEY_ID_VAR = 'AWS_ACCESS_KEY_ID'
AWS_SECRET_KEY_VAR = 'AWS_SECRET_ACCESS_KEY'

# AWS settings
AWS_SERVICE = 's3'
AWS_REGION = 'fr-par'
AWS_ENDPOINT = 'https://s3.fr-par.scw.cloud'

# Abort message
ABORT_MSG = 'AWS Credentials cannot be found as env variables, '    \
            'aborting upload.'


def get_s3_client() -> Any:
    """Setups and returns a AWS S3 session client

    :return:    S3 session client
    :rtype:     Any
    """
    aws_key_id, aws_secret_key = _get_aws_credentials()
    session = boto3.session.Session()
    s3_client = session.client(
        service_name=AWS_SERVICE,
        region_name=AWS_REGION,
        aws_access_key_id=aws_key_id,
        aws_secret_access_key=aws_secret_key,
        endpoint_url=AWS_ENDPOINT
    )
    return (s3_client)


def _get_aws_credentials() -> Tuple[str, str]:
    """Gets the AWS credentils from the env varibales.
    Exits(1) the program if they are not found.

    :return:    AWS key id and AWS secret key
    :rtype:     Tuple[str, str]
    """
    aws_key_id = os.environ.get(AWS_KEY_ID_VAR, None)
    aws_secret_key = os.environ.get(AWS_SECRET_KEY_VAR, None)
    if aws_key_id is None or aws_secret_key is None:
        print(ABORT_MSG, file=sys.stderr)
        sys.exit(1)
    aws_key_id_str: str = cast(str, aws_key_id)
    aws_secret_key_str: str = cast(str, aws_secret_key)
    return (aws_key_id_str, aws_secret_key_str)
