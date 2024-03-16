from PyPDF2 import PdfReader, PdfWriter

file_name = "AA4589561"
# full_path = "/Users/marioloeralozano/C/mix-mll/python_mix"
pdf_file = f"pdf/input_file/{file_name}.pdf"
print(f"{pdf_file=}")


inputpdf = PdfReader(open(pdf_file, "rb"))

for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    output_path = f"pdf/pages/{file_name}_{i}.pdf"
    with open(output_path, "wb") as outputStream:
        output.write(outputStream)
