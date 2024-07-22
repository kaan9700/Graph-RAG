import os
from Langchain.loaders.pdf_loader import PdfLoader
from Langchain.loaders.docx_loader import DocxLoader
from Langchain.loaders.text_loader import TxtLoader
from Langchain.loaders.image_loader import ImageLoader

class FileTypeHandler:
    def __init__(self):
        self.file_type_handlers = {
            '.docx': self.process_docx_file,
            '.txt': self.process_text_file,
            '.md': self.process_text_file,
            '.jpg': self.process_image_file,
            '.png': self.process_image_file,
            '.jpeg': self.process_image_file,
            '.gif': self.process_image_file,
            'application/pdf': self.process_pdf_file,
            '.pdf': self.process_pdf_file,
        }

    def process_docx_file(self, file_path):
        print("Processing docx file:", file_path)
        docxLoader = DocxLoader(file_path)
        pages = docxLoader.load()
        chunks = docxLoader.chunkDocument(pages, chunkSize=700)
        return chunks

    def process_text_file(self, file_path):
        # Handle text file processing logic here
        print("Processing text file:", file_path)
        textLoader = TxtLoader(file_path)
        pages = textLoader.load()
        chunks = textLoader.chunkDocument(pages, chunkSize=700)
        return chunks

    def process_pdf_file(self, file_path):
        # Handle pdf file processing logic here
        print("Processing pdf file:", file_path)
        pdfLoader = PdfLoader(file_path)
        pages = pdfLoader.load()
        chunks = pdfLoader.chunkDocument(pages, chunkSize=700)
        return chunks

    def process_image_file(self, file_path):
        # Handle image file processing logic here
        print("Processing image file:", file_path)
        imageLoader = ImageLoader(file_path)
        pages = imageLoader.load()
        chunks = imageLoader.chunkDocument(pages, chunkSize=700)
        return chunks

    def process_unknown_file(self, file_path):
        # Handle unknown file type logic here
        print("Unknown file type:", file_path)
        return LookupError("Unknown file type")

    def get_file_extension(self, file_path):
        # Use os.path.splitext() to split the path into the base and extension
        base_name, extension = os.path.splitext(file_path)
        # Return the extension (including the dot)
        return extension

    def process_file(self, file_path):
        """
        Process a file based on its extension.
        :param file_path: path to the file to be processed
        :return:
        """
        processed_files = []
        extension = self.get_file_extension(file_path)

        if extension in self.file_type_handlers:
            processed_files = self.file_type_handlers[extension](file_path)
        else:
            self.process_unknown_file(file_path)
        return processed_files
