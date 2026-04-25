import PyPDF2
import sys

def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for i, page in enumerate(reader.pages):
                text += f"\n--- Page {i+1} ---\n"
                text += page.extract_text()
            
        with open('scratch/pdf_output.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Output written to scratch/pdf_output.txt")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_pdf(sys.argv[1])
