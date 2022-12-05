from PyPDF2 import PdfReader
import svgwrite
import back.runner



def visitor_svg_rect(op, args, cm, tm):
    if op == b"re":
        (x, y, w, h) = (args[i].as_numeric() for i in range(4))
        back.runner.dwg.add(back.runner.dwg.rect((x, y), (w, h), stroke="red", fill_opacity=0.05))


def visitor_svg_text(text, cm, tm, fontDict, fontSize):
    (x, y) = (tm[4], tm[5])
    back.runner.dwg.add(back.runner.dwg.text(text, insert=(x, y), fill="blue"))



def extract(str_js):
    back.runner.dwg = svgwrite.Drawing("bagage/GeoBase_test.svg", profile="tiny")
    reader = PdfReader(str_js)
    page = reader.pages[0]
    page.extract_text(
    visitor_operand_before=visitor_svg_rect, visitor_text=visitor_svg_text
    )
    back.runner.dwg.save()