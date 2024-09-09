import PyPDF2
import sys

inputs = sys.argv[1:]  # assign all the passed arguments to inputs
print(inputs)  # inputs is a list of passed arguments


def pdf_combiner(pdf_list):
    # create a merger instance of PyPDF2
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(inputs)
