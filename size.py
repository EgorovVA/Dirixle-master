from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import RectangleObject




if __name__ == "__main__":
    reader = PdfReader("3.pdf")
    page = reader.pages[0]
    writer = PdfWriter()

    page.mediabox =  RectangleObject((
    page.mediabox.left+30,
    page.mediabox.bottom +205,
    page.mediabox.right -455,
    page.mediabox.top-3,
    ))
    writer.add_page(page)
    with open("PyPDF2-output.pdf", "wb") as fp:
        writer.write(fp)
