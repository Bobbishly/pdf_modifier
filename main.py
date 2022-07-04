import PyPDF2

with open('pdfs/dummy.pdf', 'rb') as file:
    print(file)
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    (page.rotateClockwise(90))
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('pdfs/crooked.pdf', 'wb') as file_2:
        writer.write(file_2)