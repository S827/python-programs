import PyPDF2

# with open('dummy.pdf', 'rb') as file:  # rb to read the file in binary mode
#     print(file)
#     reader = PyPDF2.PdfReader(file)  # read binary fle object
#     # get number of page by using len function on reader.pages
#     print(len(reader.pages))
#     print(reader.pages[0])  # prnts page object
#     page = reader.pages[0]  # assigns page object to page variable
#     print(page.rotate(90))  # prints page object with 90 deg rotation
#     writer = PyPDF2.PdfWriter()  # instantiate pdfWriter object
#     writer.add_page(page)  # add page to the writer object
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)  # save the writer object in tilt.pdf

with open('dummy.pdf', 'rb') as file1:
    reader = PyPDF2.PdfReader(file1)  # read binary file object
    print(len(reader.pages))
    print(reader.pages[0])
    page0 = reader.pages[0]
    # page1 = reader.pages[1]
    page0.rotate(180)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page0)
    with open('newtwopage.pdf', 'wb') as new_file1:
        writer.write(new_file1)
