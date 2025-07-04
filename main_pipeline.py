from s3_client import S3Client
from extractor_factory import get_extractor
from postgres_client import PostgresClient


BUCKET_NAME = "docs-search-bucket"
DOWNLOAD_DIR = "../data"

s3 = S3Client(bucket_name=BUCKET_NAME)
db = PostgresClient()


def run_indexing():
    
    files = s3.list_supported_files()

    for key in files:
        local_path = s3.download_file(key)
        extractor = get_extractor(local_path)
        if extractor:
            content = extractor.extract_text(local_path)
            db.index_file(key, content)


if __name__ == "__main__":
    run_indexing()