import os
import sys
import PyPDF2

source = sys.argv[1]
pdf_list = []
for name in os.listdir(source):
    pdf_list.append(name)
    with open(f"./{source}/{name}", 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(reader)


# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfMerger()
#     for pdf in pdf_list:
#         merger.append(pdf)
#     merger.write('PythonIntro.pdf')


# pdf_combiner(pdf_list)
