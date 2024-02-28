# Grobid Service Module

This module provides a Python interface to interact with the GROBID service, facilitating the processing of PDF documents into TEI (Text Encoding Initiative) XML format. GROBID (GeneRation Of BIbliographic Data) is a machine learning library to extract, parse, and re-structure raw documents (such as academic papers) into structured TEI encoded documents.

See GROBID's official docs: https://grobid.readthedocs.io/en/latest/

## Features

- **PDF Processing**: Convert PDF documents into structured TEI XML format.
- **Timeout Handling**: Customizable request timeouts to handle long-running processes gracefully.
- **Ease of Use**: Simple and intuitive API to process documents with minimal setup.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- Set up a local environment according to the root [README](../README.md)
- Access to a running a GROBID service

## Usage

To use the GrobidService in your project, import the class and initialize it with the URL of your running GROBID service. Then, call the `process_pdf` method with the path to your PDF document and the desired output path for the TEI XML file.

Example:
```python
from grobid_service import GrobidService

# Initialize the service
service = GrobidService(base_url='http://localhost:8070')

# Process a PDF and save the TEI XML
input_pdf_path = 'path/to/your/document.pdf'
output_tei_path = 'path/to/save/document.tei.xml'
service.process_pdf(input_pdf_path, output_tei_path)

print(f"TEI XML saved to {output_tei_path}")
```

## Managing GROBID Service with Docker

Included in this repository are scripts to easily start and stop the GROBID service running in Docker containers. There are options for a full GROBID service or a lightweight version.

The differences between the full and lightweight versions are explained in GROBID's documentation: https://grobid.readthedocs.io/en/latest/Run-Grobid/

### Starting GROBID Service
Full GROBID Service: Start the full GROBID service, which includes all features and capabilities, by running:
```bash
./scripts/start_grobid_full.sh
```

This script pulls the latest GROBID Docker image and starts a container named grobid_full on port 8070. Ensure your system has Docker installed and configured to use GPUs.

Lightweight GROBID Service: For quicker start-up and lower resource consumption, start the lightweight GROBID service with:
```bash
./scripts/start_grobid_lightweight.sh
```

The lightweight version also runs on port 8070, allowing easy access through your web browser or API calls.

### Stopping GROBID Service
**Full GROBID Service:** 
Stop the full GROBID service with:
```bash
./scripts/stop_grobid_full.sh
```

**Lightweight GROBID Service:** 
Stop the lightweight GROBID service with:
```bash
./scripts/stop_grobid_lightweight.sh
```
Ensure you have Docker installed and running before using these scripts.
