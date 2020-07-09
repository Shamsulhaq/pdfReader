import pyttsx3
import PyPDF2

book = open('python_tutorial.pdf','rb')  #open PDF file
pdfReader =PyPDF2.PdfFileReader(book) # init PyPDF2 by PDF
pages = pdfReader.numPages  # get total pages
speaker = pyttsx3.init() # init pyttsx3
for num in range(10,pages):
    page = pdfReader.getPage(num)   # get page
    text = page.extractText()     # get entire page text format
    speaker.say(text)          # speck text
    speaker.runAndWait()        # execute and end



