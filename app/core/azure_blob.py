
from azure.storage.blob import BlobServiceClient
from app.config import settings

class AzureBlobClient:

    def __init__(self):
        self.client = BlobServiceClient.from_connection_string(
            settings.AZURE_CONNECTION_STRING
        )
        self.container = self.client.get_container_client(
            settings.AZURE_CONTAINER
        )

    def list_files(self):
        return [blob.name for blob in self.container.list_blobs()]

    def download_file(self, blob_name):

        blob = self.container.get_blob_client(blob_name)

        return blob.download_blob().readall()
