# Prompt user for their name and output it using "fpdf2" on a shirt as a pdf


from fpdf import FPDF
from PIL import Image


class PDF(FPDF):
    def header(self):
        # Setting font
        self.set_font("helvetica", "B", 32)
        # Calculate width of the title and set cursor position
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)
        # Set color for text
        self.set_text_color(0, 0, 0)
        # Print title
        self.cell(width, 25, self.title, new_x="LMARGIN",
                    new_y="NEXT", align="C")


# Get the shirtificate.png size and then extract the width
shirt = Image.open("shirtificate.png")

pdf = PDF(orientation="portrait", format="A4")
# Set the title of the PDF as CS50 Shirtificate
pdf.set_title("CS50 Shirtificate")
# Add Page to PDF
pdf.add_page()
# Set margin to 0 so the shirt can be centered
pdf.set_margin(0)
# Add a little more space between the title and the shirt
pdf.set_y(pdf.get_y() + 10)
# Display the shirt image
pdf.image(shirt, x=((pdf.epw/2)-((pdf.epw-10)/2)), w=pdf.epw-10)
# Shirt text. Set the font, get the name and set text, then center it on the shirt
pdf.set_font("helvetica", "B", 18)
name = input("Name: ")
shirt_text = f"{name} took CS50"
width = pdf.get_string_width(shirt_text) + 6
pdf.set_x((210 - width) / 2)
pdf.set_text_color(255, 255, 255)
pdf.cell(width, -260, shirt_text, new_x="LMARGIN", new_y="NEXT", align="C")
# Save the pdf
pdf.output("shirtificate.pdf")
