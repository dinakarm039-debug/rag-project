
import json
import io
from PyPDF2 import PdfReader
import docx

class DocumentLoader:

    def load(self, file_bytes, filename):

        if filename.endswith(".pdf"):
            return self.load_pdf(file_bytes)

        if filename.endswith(".docx"):
            return self.load_docx(file_bytes)

        if filename.endswith(".txt"):
            return file_bytes.decode()

        if filename.endswith(".json"):
            return json.dumps(json.loads(file_bytes.decode()))

        return ""

    def load_pdf(self, file_bytes):

        reader = PdfReader(io.BytesIO(file_bytes))

        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text

    def load_docx(self, file_bytes):

        doc = docx.Document(io.BytesIO(file_bytes))

        return "\n".join(p.text for p in doc.paragraphs)
