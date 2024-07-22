from langchain_community.graphs import Neo4jGraph
import os
from dotenv import load_dotenv

load_dotenv()

source = input("Enter the Filename that you want to delete: ")


neo4j_uri = os.getenv("NEO4J_URI")
neo4j_username = os.getenv("NEO4J_USERNAME")
neo4j_password = os.getenv("NEO4J_PASSWORD")


graph = Neo4jGraph(url=neo4j_uri, username=neo4j_username, password=neo4j_password)

# Delete all nodes with source = "../Masterarbeit_Expose.pdf"
delete_nodes_query = """
MATCH (n)
WHERE n.source CONTAINS """ + '"' + source + '"' + """
DETACH DELETE n
"""

graph.query(delete_nodes_query)