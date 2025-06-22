
# PDFMerger

A simple Python tool to merge multiple PDF files into a single PDF document.

## Description

PDFMerger is a lightweight and easy-to-use Python script that merges multiple PDF files into one. It is useful for combining reports, scanned documents, or any PDFs that you want to consolidate.

## Features

- Merge multiple PDF files in the order specified.
- Simple command-line interface.
- Handles errors gracefully when files cannot be read.
- No external dependencies besides PyPDF2.

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

Install PyPDF2 using pip:

```
pip install PyPDF2
```

## Usage

Run the script from the command line:

```
python pdf_merger.py output.pdf input1.pdf input2.pdf [input3.pdf ...]
```

- `output.pdf` is the name of the merged PDF file to create.
- `input1.pdf`, `input2.pdf`, etc. are the PDF files to merge in order.

### Example

```
python pdf_merger.py merged.pdf chapter1.pdf chapter2.pdf appendix.pdf
```

This command merges `chapter1.pdf`, `chapter2.pdf`, and `appendix.pdf` into `merged.pdf`.

## Example Python Code Snippet

```
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
