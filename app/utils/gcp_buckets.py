from google.cloud import storage
from google.oauth2 import service_account
import requests
import uuid
import os

class BucketsClient:
    def __init__(self):
        self.credentials = service_account.Credentials.from_service_account_file(os.getenv("GCP_SERVICE_ACCOUNT"))
        self.bucket_name = os.getenv("GCP_BUCKET_NAME")
        self.client = None

    def connect(self):
        self.client = storage.Client(
                            credentials=self.credentials,
                            project=self.credentials.project_id
                        )

    def upload_image_to_bucket(self, image_url: str, image_type: str):
        image_data = requests.get(image_url).content
        filename = str(uuid.uuid4()) + "_"+ image_type + ".png"

        bucket = self.client.get_bucket(self.bucket_name)

        blob = bucket.blob(filename)
        blob.upload_from_string(image_data, content_type="image/png", timeout=300)
        return blob.public_url

async def get_bucket():
    bucket_client = BucketsClient()
    try:
        bucket_client.connect()
        yield bucket_client
    finally:
        pass