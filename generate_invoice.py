import os


def format_phone_number(value):
    if not value:
        return ''
    if len(value) == 10:
        phone = '({0}){1}-{2}'.format(value[0:3], value[3:6], value[6:10])
    elif len(value) == 11:
        phone = '+{0}({1}){2}-{3}'.format(value[0], value[1:4], value[4:7], value[7:11])
    else:
        phone = value

    return phone


def generate_pdf():  # self, request, *args, **kwargs):

    from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

    from reportlab.lib import colors
    from reportlab.lib.pagesizes import cm
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak

    doc = SimpleDocTemplate("output_commercial_invoice.pdf", rightMargin=.5 * cm, leftMargin=.5 * cm,
                            topMargin=1.5 * cm, bottomMargin=1.5 * cm)

    story = []

    # Styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
    styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='Line_Data', alignment=TA_LEFT, fontSize=8, leading=7))
    styles.add(ParagraphStyle(name='Line_Data_Small', alignment=TA_LEFT, fontSize=7, leading=8))
    styles.add(ParagraphStyle(name='Line_Data_Large', alignment=TA_LEFT, fontSize=12, leading=12))
    styles.add(ParagraphStyle(name='Line_Data_Largest', alignment=TA_LEFT, fontSize=14, leading=15))
    styles.add(ParagraphStyle(name='Line_Label', font='Helvetica-Bold', fontSize=7, leading=6, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='Line_Label_Center', font='Helvetica-Bold', fontSize=7, alignment=TA_CENTER))

    data1 = [[Paragraph('Radtek Inc.', styles["Line_Data_Large"])],
             [Paragraph('COMPANY NAME', styles["Line_Label"])],
             [Paragraph('196 Your Company Address St<br />Toronto, ON<br />L8J 1V5 CANADA', styles["Line_Data_Large"])],
             [Paragraph('COMPANY ADDRESS', styles["Line_Label"])]
    ]

    t1 = Table(data1, colWidths=(9 * cm))  #, rowHeights = [.3*cm, .5*cm, .3*cm, .5*cm])
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (0, 1), 0.25, colors.black),
        ('INNERGRID', (0, 2), (0, 3), 0.25, colors.black),
    ]))
    t1.hAlign = 'RIGHT'

    story.append(t1)

    story.append(Spacer(0.1 * cm, .5 * cm))

    story.append(Paragraph("COMMERCIAL INVOICE", styles["Line_Label_Center"]))

    data1 = [[Paragraph('INTERNATIONAL<br /> AIR WAYBILL NO.', styles["Line_Label"]),
              Paragraph('9999 9999 9999', styles["Line_Data_Largest"]),
              Paragraph('<b>NOTE: ALl shipments must be <br /> '
                        'accompanied by a Fedex Express <br /> '
                        'international Air Waybill.</b>', styles["Line_Data_Small"]),
             ]]

    t1 = Table(data1, colWidths=(3 * cm, None, 4.5 * cm,))
    t1.setStyle(TableStyle([
        ('INNERGRID', (1, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    story.append(t1)

    data1 = [[Paragraph('DATE OF EXPORTATION', styles["Line_Label"]),
              Paragraph('EXPORT REFERENCES (i.e. order no., invoice no.)', styles["Line_Label"])],
             [Paragraph('12/20/2015', styles["Line_Data_Largest"]),
              Paragraph('999432423, 14314321423', styles["Line_Data_Largest"]),
             ]]
    t1 = Table(data1)
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (1, 0), 0.25, colors.black),
        ('INNERGRID', (0, 1), (1, 1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    data1 = [[Paragraph('SHIPPER/EXPORTER (complete name and address)', styles["Line_Label"]),
              Paragraph('CONSIGNEE (complete name and address)', styles["Line_Label"])],

             [Paragraph('First, Last<br /> '
                        '196 Upper Mount Albion Address<br /> '
                        'City, Province <br /> '
                        'L8N 2V5, ON <br /> '
                        'CANADA', styles["Line_Data_Large"]),
              Paragraph('First, Last<br /> '
                        '196 Upper Mount Albion Address<br /> '
                        'City, Province <br /> '
                        'L8N 2V5, ON <br /> '
                        'CANADA', styles["Line_Data_Large"]),
             ]]
    t1 = Table(data1)
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (1, 0), 0.25, colors.black),
        ('INNERGRID', (0, 1), (1, 1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    data1 = [[Paragraph('COUNTRY OF EXPORT', styles["Line_Label"]),
              Paragraph('IMPORTER -- IF OTHER THAN CONSIGNEE <br />(complete name and address)', styles["Line_Label"])],
             [Paragraph('Country of Export', styles["Line_Data_Largest"]),
              Paragraph('First, Last<br /> '
                        '196 Upper Mount Albion Address<br /> '
                        'City, Province <br /> '
                        'L8N 2V5, ON <br /> '
                        'CANADA', styles["Line_Data_Large"])],
             [Paragraph('COUNTRY OF MANUFACTURE', styles["Line_Label"]), ''],
             [Paragraph('Country of Manufacture', styles["Line_Data_Largest"]), ''],
             [Paragraph('COUNTRY OF ULTIMATE DESTINATION', styles["Line_Label"]), ''],
             [Paragraph('Country of Ultimate Dest.', styles["Line_Data_Largest"]), ''],
    ]
    t1 = Table(data1)
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 1), (0, 2), 0.25, colors.black),
        ('INNERGRID', (0, 3), (0, 4), 0.25, colors.black),
        ('INNERGRID', (0, 0), (1, 0), 0.25, colors.black),
        ('INNERGRID', (0, 1), (1, 1), 0.25, colors.black),
        ('INNERGRID', (0, 2), (1, 2), 0.25, colors.black),
        ('INNERGRID', (0, 3), (1, 3), 0.25, colors.black),
        ('INNERGRID', (0, 4), (1, 4), 0.25, colors.black),
        ('INNERGRID', (0, 5), (1, 5), 0.25, colors.black),
        ('SPAN', (1, 1), (1, 5)),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    data1 = [[Paragraph('MARKS/NOS.', styles["Line_Label"]),
              Paragraph('NO. OF<br />PKGS.', styles["Line_Label"]),
              Paragraph('TYPE OF<br />PACKAGING', styles["Line_Label"]),
              Paragraph('FULL DESCRIPTION OF GOODS', styles["Line_Label"]),
              Paragraph('QTY.', styles["Line_Label"]),
              Paragraph('UNIT OF MEA-<br />SURE', styles["Line_Label"]),
              Paragraph('WEIGHT', styles["Line_Label"]),
              Paragraph('UNIT VALUE', styles["Line_Label"]),
              Paragraph('TOTAL<br />VALUE.', styles["Line_Label"])],
    ]

    t1 = Table(data1, colWidths=(1.7 * cm, 1.3 * cm, 2 * cm, 7 * cm, 1 * cm, 1.5 * cm, 1.5 * cm, 1.8 * cm, 1.8 * cm))
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    items = [1, 2, 3,4,5,6]  # TODO: pass items here
    data1 = [[Paragraph('1234', styles["Line_Data"]),
              Paragraph('1', styles["Line_Data"]),
              Paragraph('box', styles["Line_Data"]),
              Paragraph('a description of the goods in a full and up to date way', styles["Line_Data"]),
              Paragraph('1', styles["Line_Data"]),
              Paragraph('lbs', styles["Line_Data"]),
              Paragraph('12', styles["Line_Data"]),
              Paragraph('$30', styles["Line_Data"]),
              Paragraph('$30', styles["Line_Data"])] for item in items]
    t1 = Table(data1, colWidths=(1.7 * cm, 1.3 * cm, 2 * cm, 7 * cm, 1 * cm, 1.5 * cm, 1.5 * cm, 1.8 * cm, 1.8 * cm))
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    data1 = [['',
              Paragraph('TOTAL NO OF PKGS.', styles["Line_Label"]),
              '',
              Paragraph('TOTAL WEIGHT', styles["Line_Label"]),
              '',
              Paragraph('TOTAL INVOICE VALUE', styles["Line_Label"]),
             ],
             ['',
              Paragraph('4.', styles["Line_Data"]),
              Paragraph('SEE http://www.fedex.com FOR MORE INFORMATION ON THE CORPORATE INVOICE.',
                        styles["Line_Label_Center"]),
              Paragraph('413', styles["Line_Data"]),
              '',
              Paragraph('$420.23', styles["Line_Data"]),
             ]]
    t1 = Table(data1, colWidths=(1.7 * cm, 1.3 * cm, 11.5 * cm, 1.5 * cm, 1.8 * cm, 1.8 * cm))
    t1.setStyle(TableStyle([
        ('INNERGRID', (1, 0), (1, 1), 0.25, colors.black),
        ('INNERGRID', (3, 0), (3, 1), 0.25, colors.black),
        ('INNERGRID', (5, 0), (5, 1), 0.25, colors.black),
        ('BOX', (1, 0), (1, 1), 0.25, colors.black),
        ('BOX', (3, 0), (3, 1), 0.25, colors.black),
        ('BOX', (5, 0), (5, 1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    check_data = [[Paragraph('Check one', styles["Line_Label"]), ''],
                  [Image('images/checked.png', .25 * cm, .25 * cm), Paragraph('F.O.B.', styles["Line_Label"])],
                  [Image('images/checked.png', .25 * cm, .25 * cm), Paragraph('C & F', styles["Line_Label"])],
                  [Image('images/unchecked.png', .25 * cm, .25 * cm), Paragraph('C.I.F.', styles["Line_Label"])]]
    tc = Table(check_data, colWidths=(.4 * cm, None))
    tc.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SPAN', (0, 0), (1, 0)),
    ]))

    data1 = [[Paragraph(
        'For U.S. EXPORT ONLY: THESE COMMODITIES, TECHNOLOGY OR SOFTWARE WERE EXPORTED FROM THE UNITED STATES '
        'IN ACCORDANCE WITH THE EXPORT ADMINISTRATION REGULATIONS. DIVERSION CONTRARY TO THE UNITED STATES LAW '
        'IS PROHIBITED.', styles["Line_Label"]), '',
              tc]]
    t1 = Table(data1, colWidths=(None, 3.3 * cm, 1.8 * cm))
    t1.setStyle(TableStyle([
        ('BOX', (2, 0), (2, 0), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    story.append(Table([[Paragraph('I DECLARE THE INFORMATION CONTAINED IN THIS '
                                   'INVOICE TO BE TRUE AND CORRECT', styles["Line_Label"])]]))

    story.append(Spacer(0.1 * cm, .5 * cm))

    data1 = [
        [Paragraph('Radtek Inc.', styles["Line_Data_Large"]), '',
         Paragraph('12/24/2015', styles["Line_Data_Large"])
        ],
        [Paragraph('SIGNATURE OF SHIPPER/EXPORTER (Type name and title and sign.)', styles["Line_Label"]), '',
         Paragraph('DATE', styles["Line_Label"])]]

    t1 = Table(data1, colWidths=(None, 2*cm, None))
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (0, 1), 0.25, colors.black),
        ('INNERGRID', (2, 0), (2, 1), 0.25, colors.black),
    ]))

    story.append(t1)

    doc.build(story)


generate_pdf()