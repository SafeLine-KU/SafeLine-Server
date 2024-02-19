from google.cloud import bigquery
from google.oauth2 import service_account
import os

class BigQueryClient:
    def __init__(self):
        self.dataset_id = os.getenv("GCP_BIGQUERY_DATASET_ID")
        self.credentials = service_account.Credentials.from_service_account_file(os.getenv("GCP_SERVICE_ACCOUNT"))
        self.client = None

    def connect(self):
        self.client = bigquery.Client(
                            credentials=self.credentials,
                            project=self.credentials.project_id
                        )

    def close(self):
        if self.client:
            self.client.close()

async def get_bigquery():
    bigquery_client = BigQueryClient()
    try:
        bigquery_client.connect()
        yield bigquery_client
    finally:
        bigquery_client.close()