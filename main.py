from fpdf import FPDF
import pandas
import pathlib
import glob

filepaths = glob.glob("animals/*.txt")
# print(filepaths)
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:

    pdf.add_page()
    animal_name = pathlib.Path(filepath).stem

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=60, h=12, txt=f"{animal_name.title()}", ln=1)

    with open(filepath, "r") as file:
        description = ' '.join(file.readlines())

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=f"{description}")


pdf.output("output.pdf")




