import sys
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()

    for pdf in pdf_list:
        try:
            merger.append(pdf)
            print(f"Added: {pdf}")
        except Exception as e:
            print(f"Error adding {pdf}: {e}")

    merger.write(output_path)
    merger.close()
    print(f"Merged PDF saved as: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python pdf_merger.py output.pdf input1.pdf input2.pdf [input3.pdf ...]")
        sys.exit(1)

    output_file = sys.argv[1]
    input_files = sys.argv[2:]

    merge_pdfs(input_files, output_file)
