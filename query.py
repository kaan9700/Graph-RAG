import os
from langchain_community.vectorstores import Neo4jVector
from langchain_openai import OpenAIEmbeddings
import openai
from dotenv import load_dotenv

load_dotenv()


# Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_username = os.getenv("NEO4J_USERNAME")
neo4j_password = os.getenv("NEO4J_PASSWORD")

index_name = "vector"
store = Neo4jVector.from_existing_index(
    OpenAIEmbeddings(),
    url=neo4j_uri,
    username=neo4j_username,
    password=neo4j_password,
    index_name=index_name,
)


query = input("Enter the query: ")
results = store.similarity_search_with_score(query, k=5)

print(results)