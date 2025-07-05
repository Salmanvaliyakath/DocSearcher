from infrastructure.cloud.s3_client import S3Client
from infrastructure.index.postgress_client import PostgresClient
from utils.extractor_factory import get_extractor


BUCKET_NAME = "docs-search-bucket"
DOWNLOAD_DIR = "../data"

s3 = S3Client(bucket_name=BUCKET_NAME)
db = PostgresClient()


def run_indexing():
    
    files_in_db = db.list_file_name()
    
    s3_files = s3.list_supported_files()

    # prepare the list of files available in s3 which is not in db
    files_to_be_index = [file for file in s3_files if file not in files_in_db]

    for key in files_to_be_index:
        local_path = s3.download_file(key)
        extractor = get_extractor(local_path)
        if extractor:
            content = extractor.extract_text(local_path)
            db.index_file(key, content)


if __name__ == "__main__":
    run_indexing()