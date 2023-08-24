import boto3
from botocore.exceptions import NoCredentialsError


def generate_s3_download_url(bucket_name, object_key):
    s3_client = boto3.client('s3', aws_access_key_id='AKIA2PKCP3MNBSEF24XK',
                             aws_secret_access_key='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')
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': object_key
            },
            ExpiresIn=86400
        )
        return response
    except NoCredentialsError as err:
        print(err)
        return None


def delete_s3_object(bucket_name, object_key):
    s3_client = boto3.client('s3', aws_access_key_id='AKIA2PKCP3MNBSEF24XK',
                             aws_secret_access_key='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')
    try:
        response = s3_client.delete_object(Bucket= bucket_name, Key= object_key)
        return True
    except NoCredentialsError as err:
        print(err)
        return False
