from pypdf import PdfWriter

merger=PdfWriter()

pdfs=["pdf1.pdf","pdf2.pdf"]
for pdf in pdfs:
    merger.append(pdf)


merger.write("mergedpdf.pdf")
merger.close()
