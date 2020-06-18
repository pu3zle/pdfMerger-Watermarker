import PyPDF2
import sys

inputs = sys.argv[1:-1]
final_file = sys.argv[-1]

def pdf_merger(pdf_list, final_file):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		merger.append(pdf+".pdf")
	merger.write(final_file+".pdf")
	print("PDF's merged into {}.pdf".format(final_file))

pdf_merger(inputs, final_file)
