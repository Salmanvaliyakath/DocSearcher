import boto3
import os 

class S3Client:
    def __init__(self, bucket_name, download_dir="../data"):
        
        # Initialize an S3 client using boto3
        self.s3 = boto3.client('s3')

        # Store the S3 bucket name to interact with
        self.bucket_name = bucket_name

        # Directory path where files downloaded from S3 will be saved locally
        self.download_dir = download_dir

        # Create the download directory if it does not exist
        os.makedirs(download_dir, exist_ok=True)

    def list_supported_files(self):
        """
        List all files in the specified S3 bucket that have supported extensions.
        
        Returns:
            List of file keys (paths) in the bucket ending with .txt, .pdf, .csv, or .png
        """
        response = self.s3.list_objects_v2(Bucket=self.bucket_name)
        files = response.get('Contents', [])
        return [f['Key'] for f in files if f['Key'].endswith(('.txt', '.pdf', '.csv', '.png'))]

    def download_file(self, s3_key):
        """
        Download a file from S3 to the local download directory.
        
        Args:
            s3_key (str): The key (path) of the file in the S3 bucket to download.
        
        Returns:
            The local path where the file is saved.
        """
        local_path = os.path.join(self.download_dir, os.path.basename(s3_key))
        self.s3.download_file(self.bucket_name, s3_key, local_path)
        return local_path