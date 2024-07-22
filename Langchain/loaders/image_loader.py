import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from Langchain.schema.loaders import Loaders
from typing import Union, List
from langchain.docstore.document import Document
from openai import OpenAI
from dotenv import load_dotenv
import base64

# Load the environment variables from the .env file
load_dotenv()

class ImageLoader(Loaders):
    def __init__(self, file_path: str):
        """
        Initialize ImageLoader

        :param file_path: The path to the file to be loaded
        """
        self.file_path = file_path
        if "~" in self.file_path:
            self.file_path = os.path.expanduser(self.file_path)

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def get_image_text(self):
        base64_image = self.encode_image(self.file_path)
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe the image in detail."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
        )

        if response.choices[0].message.content:
            return response.choices[0].message.content
        else:
            raise Exception("Failed to get a valid response from the model")


    def load(self) -> Union[str, List[str], List[Document]]:
        """Load content from an image and return it
            :return: The content of the image as a pagewise list of Langchain Documents
        """
        try:
            image_text = self.get_image_text()
            return image_text

        except Exception as e:
            return f"Error loading image text: {str(e)}"




    def chunkDocument(self, document: str, chunkSize=750) -> List[Document]:
        """Chunk a document into smaller parts for processing via embeddings
        :param document: The document to be chunked (generated by load())
        :param chunkSize: The size of the chunks (default 750), greatly affects the result of the embeddings & prompts
        :return: The chunked document as a list of Langchain Documents with metadata [page, source, start_index]
        """

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunkSize,
            chunk_overlap=20,
            add_start_index=True,
        )

        chunked_content = [
            Document(
                page_content=x,
                metadata={'source': f'{self.file_path}'}
            ) for x in text_splitter.split_text(document)
        ]

        return chunked_content

