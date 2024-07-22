# Graph-Rag

## Project description
Graph-RAG implements a simple approach of a Graph RAG. The project makes it possible to specify a document path via the command line input. The file, if the file type is supported (PDF, Docx, JPG, TXT or MD), is chunked and embedded. This data is then saved in a Neo4j database.

## Functions and features
- Document insertion: Files can be inserted into the Neo4j database using insert_docs.py. 


- Document deletion: Files can be deleted from the Neo4j database using delete_docs.py. 


- Similarity search: A third script can be used to enter a prompt that performs a similarity search on the graph database and outputs the corresponding documents.

## Installation
1. ### Clone das Repository:
```bash
git clone https://github.com/yourusername/Graph-RAG.git
cd Graph-RAG
```
2. ### Python Version:

    Make sure that Python 3.11.9 is installed.

3. ### Install dependencies:
    Install the required dependencies from the requirements.txt:
```bash
pip install -r requirements.txt
```



