import boto3
import os 

class S3Client:
    def __init__(self, bucket_name, download_dir="../data"):
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name
        self.download_dir = download_dir
        os.makedirs(download_dir, exist_ok=True)

    def list_supported_files(self):
        response = self.s3.list_objects_v2(Bucket=self.bucket_name)
        files = response.get('Contents', [])
        return [f['Key'] for f in files if f['Key'].endswith(('.txt', '.pdf', '.csv', '.png'))]

    def download_file(self, s3_key):
        local_path = os.path.join(self.download_dir, os.path.basename(s3_key))
        self.s3.download_file(self.bucket_name, s3_key, local_path)
        return local_path