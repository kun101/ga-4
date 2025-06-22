import pdfplumber
import subprocess
import sys
import os

def extract_text_from_pdf(pdf_path):
    """Extract text content from PDF using pdfplumber."""
    all_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                all_text.append(text)
    return "\n\n".join(all_text)

def simple_text_to_markdown(text):
    """
    Basic conversion of extracted text to markdown.
    This is a simple placeholder - more advanced logic can be added based on document structure.
    """
    # Example: Convert lines starting with "Chapter", "Section" to headers
    md_lines = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("Chapter "):
            md_lines.append(f"# {line}")
        elif line.startswith("Section "):
            md_lines.append(f"## {line}")
        elif line.isupper() and len(line.split()) < 6:
            # Assume uppercase short lines are headings
            md_lines.append(f"### {line.title()}")
        else:
            md_lines.append(line)
    return "\n\n".join(md_lines)

def format_markdown_with_prettier(md_file_path):
    """Formats the Markdown file using Prettier 3.4.2 CLI."""
    try:
        subprocess.run(
            ["prettier", "--write", md_file_path],
            check=True
        )
        print(f"Markdown formatted with Prettier: {md_file_path}")
    except subprocess.CalledProcessError as e:
        print("Error running Prettier:", e)
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_markdown.py <input_pdf_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    if not os.path.isfile(pdf_path):
        print(f"File not found: {pdf_path}")
        sys.exit(1)

    print(f"Extracting text from PDF: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)
    print("Converting extracted text to Markdown...")
    markdown = simple_text_to_markdown(text)

    md_file_path = os.path.splitext(pdf_path)[0] + ".md"
    with open(md_file_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"Markdown saved to: {md_file_path}")
    print("Formatting Markdown with Prettier 3.4.2...")
    format_markdown_with_prettier(md_file_path)

if __name__ == "__main__":
    main()
