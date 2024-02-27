"""
This module provides a service for processing PDF documents through the GROBID
service. GROBID (GeneRation Of BIbliographic Data) extracts, parses, and
restructures raw documents (such as PDFs) into structured TEI (Text Encoding
Initiative) encoded documents with a particular focus on technical and
scientific publications.
"""
from typing import Tuple

import requests

class GrobidService:
  """
  A service class for interacting with a GROBID server to process PDF
  documents and convert them into structured TEI format.

  Attributes:
      base_url (str): The base URL of the GROBID server.
  """

  def __init__(self, base_url: str = "http://localhost:8070"):
    self.base_url: str = base_url

  def process_pdf(
      self,
      input_pdf_path: str,
      output_tei_path: str,
      timeout: Tuple[int, int] = (10, 300)
  ) -> str:
    """
    Processes a PDF file through the GROBID service and saves the output in TEI
    format.

    This method sends the specified PDF to the GROBID server for processing and
    saves the resulting TEI XML to a specified file path. It includes
    handling for request timeouts.

    Args:
        input_pdf_path (str): The file path of the input PDF to be processed.
        output_tei_path (str): The file path where the TEI output should be
        saved.
        timeout (tuple): A tuple specifying the connect and read timeout in
        seconds.

    Returns:
        str: The TEI XML string returned by the GROBID service or an error
        message if a timeout occurs.

    Note:
        The 'file' variable within the 'with' block for reading the PDF is
        expected to be of type BinaryIO.
    """
    try:
      with open(input_pdf_path, "rb") as file:
        files = {"input": (input_pdf_path, file, "application/pdf")}
        response = requests.post(
          f"{self.base_url}/api/processFulltextDocument",
          files=files,
          timeout=timeout
        )

      with open(output_tei_path, "w", encoding="utf-8") as output_file:
        output_file.write(response.text)

      return response.text
    except TimeoutError:
      error_message = "The request timed out."
      print(error_message)
      return error_message


if __name__ == "__main__":
  service = GrobidService()
  input_path: str = "../../input_pdfs/Advanced Automotive Fault Diagnosis.pdf"
  output_path: str = "../../output_xmls/Advanced Automotive Fault Diagnosis.xml"
  service.process_pdf(input_path, output_path)
  print(f"Processed PDF saved to {output_path}")
