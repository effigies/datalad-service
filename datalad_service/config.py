"""Environment based configuration."""
import os
import sys


def get_environ(key, fallback=None):
    """Get a key from the environment and set it on this module (or a fallback value)."""
    return os.environ[key] if key in os.environ else fallback


# Configuration specific to the datalad-service
DATALAD_WORKERS = get_environ('DATALAD_WORKERS', 1)
DATALAD_GITHUB_ORG = get_environ('DATALAD_GITHUB_ORG')
DATALAD_GITHUB_LOGIN = get_environ('DATALAD_GITHUB_LOGIN')
DATALAD_GITHUB_PASS = get_environ('DATALAD_GITHUB_PASS')

# Configuration shared with OpenNeuro or AWS CLI
AWS_ACCESS_KEY_ID = get_environ('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_environ('AWS_SECRET_ACCESS_KEY')
AWS_REGION = get_environ('AWS_REGION')
AWS_ACCOUNT_ID = get_environ('AWS_ACCOUNT_ID')
AWS_S3_PRIVATE_BUCKET = get_environ('AWS_S3_PRIVATE_BUCKET')
AWS_S3_PUBLIC_BUCKET = get_environ('AWS_S3_PUBLIC_BUCKET')
