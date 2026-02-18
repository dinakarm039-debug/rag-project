import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

import uuid
from app.core.azure_blob import AzureBlobClient
from app.loaders.document_loader import DocumentLoader
from app.utils.text_splitter import TextSplitter
from app.core.embeddings import Embeddings
from app.core.pinecone_db import PineconeDB

blob = AzureBlobClient()
loader = DocumentLoader()
splitter = TextSplitter()
embedder = Embeddings()
db = PineconeDB()

files = blob.list_files()

for file in files:

    print("Processing", file)

    data = blob.download_file(file)

    text = loader.load(data, file)

    chunks = splitter.split(text)

    vectors = []

    for chunk in chunks:

        vector = embedder.embed(chunk)

        vectors.append({
            "id": str(uuid.uuid4()),
            "values": vector,
            "metadata": {"text": chunk}
        })

    db.upsert(vectors)

print("Ingestion Complete")
