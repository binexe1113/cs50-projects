from fpdf import FPDF

def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.image("shirtificate.png", x=10, y=10, w=100)
    pdf.output("test.pdf")

if __name__ == "__main__":
    main()
