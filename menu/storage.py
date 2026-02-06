from storages.backends.s3boto3 import S3Boto3Storage

class SupabaseMediaStorage(S3Boto3Storage):
    location = "media_fast_food"
    file_overwrite = False
