#unionepdf help you to join .pdf files
#pip install PyPDF4
#join PDF files


import os

from PyPDF4 import PdfFileMerger

source_dir = os.getcwd()
merger = PdfFileMerger()

for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        merger.append(item)

merger.write('./File_unito.pdf')       
merger.close()