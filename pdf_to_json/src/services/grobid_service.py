
import requests

class GrobidService:
    def __init__(self, base_url='http://localhost:8070'):
        self.base_url = base_url

    def process_pdf(self, pdf_path):
        # Example method to process a PDF through GROBID
        with open(pdf_path, 'rb') as file:
            files = {'input': (pdf_path, file, 'application/pdf')}
            response = requests.post(f'{self.base_url}/api/processFulltextDocument', files=files)
            return response.text

# Usage example
if __name__ == '__main__':
    service = GrobidService()
    result = service.process_pdf('/home/hofbr/GitProjects/second-opinion/Advanced Automotive Fault Diagnosis (1).pdf')
    print(result)
