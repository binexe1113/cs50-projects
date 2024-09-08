from fpdf import FPDF
from fpdf.enums import XPos, YPos

def main():
    inp = input("What on shirt? ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=13)
    pdf.image("shirtificate.png", x=10, y=10, w=100)
    pdf.set_xy(48, 55)
    pdf.cell(20, 10, text=inp, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
