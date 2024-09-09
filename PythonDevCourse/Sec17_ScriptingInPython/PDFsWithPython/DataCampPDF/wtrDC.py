import PyPDF2

template = PyPDF2.PdfReader(open('PythonIntro.pdf', 'rb'))
print(template)
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

watermark_page = watermark.pages[0]
for i in range(len(template.pages)):
    original_page = template.pages[i]

    # merge the watermark page on top of blank page
    blank_page = PyPDF2.PageObject.create_blank_page(
        width=original_page.mediabox.width,
        height=original_page.mediabox.height
    )
    blank_page.merge_page(watermark_page)
    blank_page.merge_page(original_page)
    output.add_page(blank_page)
    with open('wtrPyIntro.pdf', 'wb') as file:
        output.write(file)
