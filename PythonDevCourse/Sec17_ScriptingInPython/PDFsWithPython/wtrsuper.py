import PyPDF2

template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
print(template)
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
print(watermark)
output = PyPDF2.PdfWriter()
print(template.pages[0])
for i in range(len(template.pages)):
    print(i)
    page = template.pages[i]
    print(page)
    page.merge_page(watermark.pages[0])
    print(page)
    output.add_page(page)
    print(output)
    with open('wtr_out.pdf', 'wb') as file:
        output.write(file)
