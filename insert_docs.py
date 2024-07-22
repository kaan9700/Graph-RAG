from langchain_community.graphs import Neo4jGraph
from langchain_community.vectorstores import Neo4jVector

from Langchain.utils.FileTypeHandler import FileTypeHandler
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import openai
import os

load_dotenv()


# Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_username = os.getenv("NEO4J_USERNAME")
neo4j_password = os.getenv("NEO4J_PASSWORD")

file_location = input("Enter the file location: ")

filehandler = FileTypeHandler()

docs = filehandler.process_file(file_location)
# ~/Desktop/Masterarbeit_expose.pdf
print(docs)


# Initialize Neo4j connection
graph = Neo4jGraph(
    url=neo4j_uri,
    username=neo4j_username,
    password=neo4j_password,
)

# Generate embeddings
embeddings = OpenAIEmbeddings()

# Store documents and embeddings in Neo4j
neo4j_vector = Neo4jVector.from_documents(docs, embeddings, url=neo4j_uri, username=neo4j_username, password=neo4j_password)



