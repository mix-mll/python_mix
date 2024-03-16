from pdf2image import convert_from_path

file_name = "X"
pdf_file = f"pdf/input_file/{file_name}.pdf"
output_path = "pdf/pages"

pages = convert_from_path(pdf_file, 500)

for count, page in enumerate(pages):
    page.save(f"{output_path}/{file_name}_{count}.jpg", "JPEG")
