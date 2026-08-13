

#This is py first project

from PyPDF2 import PdfMerger


marge = PdfMerger()

# for i in ["ICT Assinment.pdf","Vocabulary.pdf"]:
#     marge.append(i)
marge.append("Vocabulary.pdf",pages=(0,4,1))
marge.append("ICT Assinment.pdf",pages= (0,5,1))

marge.write("Mrittika.pdf")
marge.close()