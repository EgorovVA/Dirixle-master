from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import RectangleObject

def pars_size(file):#+drop return get_size_square
    reader = PdfReader(file)
    page = reader.pages[0]
    writer = PdfWriter()
    width = int(float(page.mediaBox.getWidth()))#841 for 3.pdf
    height = int(float(page.mediaBox.getHeight()))#595 for 3.pdf
    page.mediabox =  RectangleObject((
    page.mediabox.left+30,
    page.mediabox.bottom +205,
    page.mediabox.right -455,
    page.mediabox.top-3,
    ))
    writer.add_page(page)
    with open("pars_size.pdf", "wb") as fp:
        writer.write(fp)


if __name__ == "__main__":
    pars_size("3.pdf")


