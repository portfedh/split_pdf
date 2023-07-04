from PyPDF2 import PdfReader

class SeparatePDF():

    def __init__(self):
        self.file = 'file.pdf'
        self.open_files()
        self.check_pages()
        self.separate_pages()

    def open_files(self):
        self.oppen_file = PdfReader(open(self.file, 'rb'))

    def check_pages(self):
        self.file_pages = len(self.oppen_file.pages)
        print("The number of pages in the pdf is: "+str(self.file_pages))

    def separate_pages(self):
        for x in range(self.file_pages):
            print("Printing page number: "+str(x))


if __name__ == '__main__':
    oMerge = SeparatePDF()
