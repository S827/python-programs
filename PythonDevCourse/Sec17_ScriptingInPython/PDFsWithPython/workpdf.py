import PyPDF2

with open('dummy.pdf', 'rb') as file:  # rb to read the file in binary mode
    print(file)
    reader = PyPDF2.PdfReader(file)  # read binary fle object
    # get number of page by using len function on reader.pages
    print(len(reader.pages))
    print(reader.pages[0])
    page = reader.pages[0]
    print(page.rotate(90))
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

with open('twopage.pdf', 'rb') as file1:
    reader = PyPDF2.PdfReader(file1)
    print(len(reader.pages))
    print(reader.pages[1])
