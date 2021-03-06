from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus.flowables import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from pdf_turtle import PdfTurtle


def create_drawing(scale=1.0):
    t = PdfTurtle.create(600, 600)
    t.fillcolor('blue')
    t.begin_fill()
    for i in range(20):
        d = (50 + i*i*1.5)
        t.pencolor(0, 0.05*i, 0)
        t.width(i)
        t.forward(d)
        t.right(144)
    t.end_fill()

    drawing = t.to_reportlab()

    # Scale the Drawing.
    drawing.scale(scale, scale)
    drawing.width *= scale
    drawing.height *= scale
    return drawing


def go():
    doc = SimpleDocTemplate("example.pdf")
    styles = getSampleStyleSheet()
    story = [Paragraph('PDF Example', styles['Title'])]
    text = """\
This is an example of how to use turtle graphics in a PDF document."""
    story.append(Paragraph(text, styles['Normal']))
    story.append(Spacer(1, 0.055*inch))
    story.append(create_drawing(scale=0.75))
    story.append(Paragraph("You can control the size of a graphic.",
                           styles['Normal']))
    story.append(Spacer(1, 0.055*inch))
    story.append(create_drawing(scale=0.25))
    story.append(Paragraph("Try creating your own documents.",
                           styles['Normal']))
    doc.build(story)


go()

# Uncomment this to display the PDF after you generate it.
# from subprocess import call  # @IgnorePep8
# call(["evince", "example.pdf"])
