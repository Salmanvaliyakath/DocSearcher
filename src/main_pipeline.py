from infrastructure.cloud.s3_client import S3Client
from infrastructure.index.postgress_client import PostgresClient
from utils.extractor_factory import get_extractor

# Constants for S3 bucket name and local download directory
BUCKET_NAME = "docs-search-bucket"
DOWNLOAD_DIR = "../data"

# Initialize the S3 client with the target bucket
s3 = S3Client(bucket_name=BUCKET_NAME)

# Initialize the PostgreSQL client
db = PostgresClient()


def run_indexing():

    """
    Downloads and indexes new files from S3 into PostgreSQL
    if they are not already present in the database.
    """
    
    # Get a list of files already indexed in the database
    files_in_db = db.list_file_name()
    
    # Get a list of supported files available in the S3 bucket
    s3_files = s3.list_supported_files()

    # Identify files that exist in S3 but not in the database
    files_to_be_index = [file for file in s3_files if file not in files_in_db]

    for key in files_to_be_index:

        # Download the file from S3 to the local directory
        local_path = s3.download_file(key)

        # Get an appropriate extractor instance based on the file type
        extractor = get_extractor(local_path)

        # If an extractor was found, extract the text content and index it in the database
        if extractor:
            content = extractor.extract_text(local_path)
            db.index_file(key, content)

# Entry point
if __name__ == "__main__":
    run_indexing()