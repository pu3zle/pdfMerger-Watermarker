import PyPDF2
import sys


file = sys.argv[1]
wtr = sys.argv[2]
out = sys.argv[3]

template = PyPDF2.PdfFileReader(open(file+".pdf", 'rb'))
watermark = PyPDF2.PdfFileReader(open(wtr+".pdf", 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)
	
with open(out+".pdf", 'wb') as file:
	output.write(file)
print("Watermarked version saved in {}.pdf".format(out))
