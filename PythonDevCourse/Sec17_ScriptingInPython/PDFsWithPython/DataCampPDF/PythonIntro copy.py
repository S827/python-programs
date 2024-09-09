import os
import sys
import PyPDF2

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('PythonIntro.pdf')


pdf_combiner(inputs)
