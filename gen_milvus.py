import os

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.vectorstores import Milvus
from langchain_openai import OpenAIEmbeddings


def create_db():
    loader = UnstructuredPDFLoader("Advanced Automotive Fault Diagnosis.pdf")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=150, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    Milvus.from_documents(texts, embeddings, collection_name="car", connection_args={"host": "localhost", "port": 19530})


if __name__ == '__main__':
    create_db()